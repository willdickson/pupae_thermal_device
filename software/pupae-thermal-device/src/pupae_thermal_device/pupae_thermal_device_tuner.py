from PySide6 import QtCore
from PySide6 import QtWidgets
from .ui_tuner_main_window import Ui_TunerMainWindow
from .device_connection_dialog import DeviceConnectionDialog
from .device_information_dialog import DeviceInformationDialog
from .pupae_thermal_device import PupaeThermalDevice
from .status_info import StatusInfo

class TunerMainWindow(QtWidgets.QMainWindow, Ui_TunerMainWindow):

    TEXT_CONNECTED = 'connected to'
    TEXT_NOT_CONNECTED = 'not connected'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection_dialog = DeviceConnectionDialog(self)
        self.device_information_dialog = DeviceInformationDialog(self)
        self.initialize()
        self.setup_connections()
        self.device = None
        self.port_name = ''

    def initialize(self):
        self.disable_widgets_on_disconnect()
        self.status_info = StatusInfo()
        self.status_bar = self.statusBar()
        self.status_bar.addPermanentWidget(self.status_info,1)
        self.status_info.set_text(self.TEXT_NOT_CONNECTED)

    def setup_connections(self):
        self.action_device_connection.triggered.connect(self.on_action_device_connection)
        self.action_device_information.triggered.connect(self.on_action_device_information)
        self.connection_dialog.sig_opened.connect(self.slot_device_opened)
        self.connection_dialog.sig_closed.connect(self.slot_device_closed)
        self.controller_parameters_widget.connect_device_open_close_slots(self.connection_dialog)

    @QtCore.Slot(PupaeThermalDevice,str)
    def slot_device_opened(self, device, port_name):
        self.device = device
        self.port_name = port_name
        self.action_device_information.setEnabled(True)
        self.enable_widgets_on_connect()
        self.set_status_connected(port_name)

        hardware_version = 'not done'
        firmware_version = 'not done'
        self.device_information_dialog.hardware_version = hardware_version
        self.device_information_dialog.firmware_version = firmware_version


    @QtCore.Slot()
    def slot_device_closed(self):
        self.device = None
        self.port_name = ''
        self.action_device_information.setEnabled(False)
        self.disable_widgets_on_disconnect()
        self.set_status_disconnected()
        self.device_information_dialog.hardware_version = ''
        self.device_information_dialog.firmware_version = ''


    def set_status_connected(self, port_name):
        status_text = f'{self.TEXT_CONNECTED} {port_name}'
        self.status_info.set_text(status_text)

    def set_status_disconnected(self):
        self.status_info.set_text('not connected')

    def disable_widgets_on_disconnect(self):
        self.action_device_information.setEnabled(False)
        self.action_file_save_data.setEnabled(False)
        self.action_file_save_figure.setEnabled(False)
        self.controller_parameters_groupbox.setEnabled(False)
        self.system_values_groupbox.setEnabled(False)
        self.plot_groupbox.setEnabled(False)


    def enable_widgets_on_connect(self):
        self.controller_parameters_groupbox.setEnabled(True)
        self.system_values_groupbox.setEnabled(True)
        self.plot_groupbox.setEnabled(True)


    def on_action_device_connection(self):
        self.connection_dialog.show()


    def on_action_device_information(self):
        self.device_information_dialog.show()
