import serial
import serial.tools.list_ports
from collections import OrderedDict
from PySide6 import QtCore
from PySide6 import QtWidgets
from .ui_device_connection_dialog import Ui_DeviceConnectionDialog
from .pupae_thermal_device import PupaeThermalDevice 


class DeviceConnectionDialog(Ui_DeviceConnectionDialog, QtWidgets.QDialog):

    PORT_LIST_TIMER_DT = 4000
    OPEN_CONNECTION_STR = 'Connect'
    CLOSE_CONNECTION_STR = 'Disconnect'

    sig_opened = QtCore.Signal(PupaeThermalDevice,str)
    sig_closed = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.initialize()
        self.setup_connections()
        self.port_name_to_info = OrderedDict()
        self.device = None
        self.update_port_list()

    def showEvent(self, event):
        super().showEvent(event)
        if self.device is None:
            self.timer.start(self.PORT_LIST_TIMER_DT)

    def hideEvent(self, event):
        super().hideEvent(event)
        self.timer.stop()

    def initialize(self):
        self.set_button_text_to_open_connection()
        self.filter_checkbox.setCheckState(QtCore.Qt.Checked)

    def setup_connections(self):
        self.timer.timeout.connect(self.on_timer)
        self.connect_pushbutton.clicked.connect(self.on_connect_clicked)
        self.port_combobox.currentTextChanged.connect(self.on_port_combobox_changed)
        self.port_combobox.setDuplicatesEnabled(False)
        self.filter_checkbox.checkStateChanged.connect(self.on_filter_checkstate_changed)
        self.close_dialog_pushbutton.clicked.connect(self.on_close_dialog)

    def update_port_list(self):
        # Save the old list of serial port names - used to check if we need to update combobox
        old_port_name_list = list(self.port_name_to_info.keys())
        # Get list of (current) serial ports and (optionally) remove those without vid or pid
        port_list = serial.tools.list_ports.comports()
        if self.filter_checkbox.checkState() == QtCore.Qt.Checked:
            port_list = [p for p in port_list if p.vid is not None or p.pid is not None]
        # Create table relating serial port name to serial port info
        port_name_info_list = sorted([(p.device, p) for p in port_list])
        self.port_name_to_info = OrderedDict(port_name_info_list)
        # Compare old list of port names to new list of ports names. If list has changed
        # update the combobox 
        port_name_list = [name for name, _ in port_name_info_list] 
        if port_name_list != old_port_name_list:
            self.port_combobox.clear()
            self.port_combobox.insertItems(0, port_name_list)

    def on_timer(self):
        self.update_port_list()

    def on_close_dialog(self):
        self.hide()

    def on_connect_clicked(self):
        current_device_name = self.port_combobox.currentText()
        if self.device is None:
            self.timer.stop()
            try:
                self.device = PupaeThermalDevice(current_device_name)
            except Exception as err:
                print('unable to connect')
                title = 'Connection Error'
                message = f'unable to connect: {err}'
                messgebox = QtWidgets.QMessageBox.warning(self, title, message)
                self.timer.start()
            else:
                self.port_combobox.setEnabled(False)
                self.set_button_text_to_close_connection()
                self.sig_opened.emit(self.device, current_device_name)
        else:
            self.device.close()
            self.device = None
            self.port_combobox.setEnabled(True)
            self.set_button_text_to_open_connection()
            self.timer.start(self.PORT_LIST_TIMER_DT)
            self.sig_closed.emit()
        self.update_port_info(current_device_name)

    def on_port_combobox_changed(self, device_name):
        if not device_name:
            return
        self.update_port_info(device_name)

    def on_filter_checkstate_changed(self, state):
        self.update_port_list()

    def set_button_text_to_open_connection(self):
        self.connect_pushbutton.setText(self.OPEN_CONNECTION_STR)

    def set_button_text_to_close_connection(self):
        self.connect_pushbutton.setText(self.CLOSE_CONNECTION_STR)

    def create_port_info_str(self, device_name):
        if not device_name:
            return
        port_info = self.port_name_to_info[device_name]
        port_info_list = []
        port_info_list.append(f'Product: {port_info.product}')
        port_info_list.append(f'Manufacturer: {port_info.manufacturer}')
        port_info_list.append(f'Serial #:  {port_info.serial_number}')
        port_info_list.append(f'VID:  {hex_str(port_info.vid)}')
        port_info_list.append(f'PID:  {hex_str(port_info.pid)}')
        if self.device is not None:
            port_info_list.append('Connected')
        else:
            port_info_list.append('Not Connected')

        port_info_str = '\n'.join(port_info_list)
        return port_info_str


    def update_port_info(self, device_name):
        port_info_str = self.create_port_info_str(device_name)
        self.port_info_label.setText(port_info_str)

    def clear_port_info(self):
        self.port_info_label.setText('')


# Utility
# ----------------------------------------------------------------------------
def hex_str(val):
    try:
       val_str = f'0x{val:0X}'
    except TypeError:
        val_str = f'{val}'
    return val_str



