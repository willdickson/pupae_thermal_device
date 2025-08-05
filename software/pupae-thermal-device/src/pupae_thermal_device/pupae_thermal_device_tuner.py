import time
from PySide6 import QtCore
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT 
from .ui_tuner_main_window import Ui_TunerMainWindow
from .device_connection_dialog import DeviceConnectionDialog
from .device_information_dialog import DeviceInformationDialog
from .pupae_thermal_device import PupaeThermalDevice
from .status_info import StatusInfo
from .mplcanvas import MplCanvas

class TunerMainWindow(QtWidgets.QMainWindow, Ui_TunerMainWindow):

    TIMER_DT = 100 
    TEXT_CONNECTED = 'connected to'
    TEXT_NOT_CONNECTED = 'not connected'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection_dialog = DeviceConnectionDialog(self)
        self.device_information_dialog = DeviceInformationDialog(self)
        self.timer = QtCore.QTimer()
        self.initialize()
        self.setup_connections()
        self.device = None
        self.port_name = ''
        self.plot_data = create_empty_plot_data() 
        self.t_start = time.time()
        self.t_last = self.t_start

    def initialize(self):
        self.disable_widgets_on_disconnect()
        self.status_info = StatusInfo()
        self.status_bar = self.statusBar()
        self.status_bar.addPermanentWidget(self.status_info,1)
        self.status_info.set_text(self.TEXT_NOT_CONNECTED)
        self.timer.setInterval(self.TIMER_DT)

        self.plot_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.plot_toolbar = NavigationToolbar2QT(self.plot_canvas, self)
        self.plot_layout = QtWidgets.QVBoxLayout()
        self.plot_layout.addWidget(self.plot_toolbar)
        self.plot_layout.addWidget(self.plot_canvas)
        self.plot_area_widget.setLayout(self.plot_layout)
        self.plot_canvas.set_plot_time_window(self.plot_settings_widget.window)
        self.plot_canvas.draw()

    def setup_connections(self):
        self.action_device_connection.triggered.connect(self.on_action_device_connection)
        self.action_device_information.triggered.connect(self.on_action_device_information)
        self.connection_dialog.sig_opened.connect(self.slot_device_opened)
        self.connection_dialog.sig_closed.connect(self.slot_device_closed)
        self.controller_parameters_widget.connect_device_open_close_slots(self.connection_dialog)
        self.timer.timeout.connect(self.on_timer)
        self.plot_settings_widget.sig_plot_window_changed.connect(self.plot_window_changed)
        self.plot_settings_widget.sig_plot_window_reset.connect(self.plot_window_reset)
        self.controller_parameters_widget.sig_setpoint_left_changed.connect(
                self.plot_canvas.set_setpoint_left
                )
        self.controller_parameters_widget.sig_setpoint_right_changed.connect(
                self.plot_canvas.set_setpoint_right
                )

    def on_timer(self):
        device_values = self.device.get_all()
        self.system_values_widget.set_values(device_values)
        if self.controller_parameters_widget.setpoint != tuple(device_values['ctrl_setpoint']):
            self.controller_parameters_widget.setpoint = device_values['ctrl_setpoint']
        self.update_plot_data(device_values)
        self.plot_canvas.update_plot_lines(self.plot_data)
        self.plot_canvas.draw()

    def update_plot_data(self, device_values):
        t_now = time.time()
        t = t_now - self.t_start
        dt = t_now - self.t_last
        self.t_last = t_now
        print(f't: {t:.2f}, dt: {dt:.3f}')

        pgain_right = device_values['ctrl_pgain'][0]
        pgain_left = device_values['ctrl_pgain'][1]
        igain_right = device_values['ctrl_igain'][0]
        igain_left = device_values['ctrl_igain'][1]
        setpoint_right = device_values['ctrl_setpoint'][0]
        setpoint_left = device_values['ctrl_setpoint'][1]
        temperature_right = device_values['temperature'][0]
        temperature_left = device_values['temperature'][1]
        error_right = device_values['ctrl_error'][0]
        error_left = device_values['ctrl_error'][1]
        ierror_right = device_values['ctrl_ierror'][0]
        ierror_left = device_values['ctrl_ierror'][1]
        power_right = device_values['ctrl_power'][0]
        power_left = device_values['ctrl_power'][1]

        self.plot_data['t'].append(t)
        self.plot_data['temperature']['right'].append(temperature_right)
        self.plot_data['temperature']['left'].append(temperature_left)
        self.plot_data['setpoint']['right'].append(setpoint_right)
        self.plot_data['setpoint']['left'].append(setpoint_left)
        self.plot_data['error']['right'].append(pgain_right*error_right)
        self.plot_data['error']['left'].append(pgain_right*error_left)
        self.plot_data['ierror']['right'].append(igain_left*ierror_right)
        self.plot_data['ierror']['left'].append(igain_left*ierror_left)
        self.plot_data['power']['right'].append(power_right)
        self.plot_data['power']['left'].append(power_left)

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
        self.t_start = time.time()
        self.t_last = self.t_start
        self.timer.start()

    @QtCore.Slot()
    def slot_device_closed(self):
        self.device = None
        self.port_name = ''
        self.action_device_information.setEnabled(False)
        self.disable_widgets_on_disconnect()
        self.set_status_disconnected()
        self.device_information_dialog.hardware_version = ''
        self.device_information_dialog.firmware_version = ''
        self.timer.stop()

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

    def plot_window_changed(self, new_value):
        self.plot_canvas.set_plot_time_window(new_value)

    def plot_window_reset(self):
        self.plot_data = create_empty_plot_data()
        self.t_start = time.time()
        self.t_last = self.t_start

# Utility
# --------------------------------------------------------------------------------

def create_empty_plot_data(): 
    plot_data = { 
            't'           : [],
            'temperature' : {'right' : [], 'left' : []},
            'setpoint'    : {'right' : [], 'left' : []},
            'error'       : {'right' : [], 'left' : []}, 
            'ierror'      : {'right' : [], 'left' : []},
            'power'       : {'right' : [], 'left' : []}, 
            } 
    return plot_data
