from PySide6 import QtCore
from PySide6 import QtWidgets
from .ui_controller_parameters_widget import Ui_ControllerParametersWidget
from .pupae_thermal_device import PupaeThermalDevice


class ControllerParametersWidget(QtWidgets.QWidget, Ui_ControllerParametersWidget):

    TEXT_ENABLED = 'Enabled'
    TEXT_DISABLED = 'Disabled'

    sig_setpoint_left_changed = QtCore.Signal(float)
    sig_setpoint_right_changed = QtCore.Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initialize()
        self.setup_connections()
        self.device = None

    def initialize(self):
        self.set_enable_disable_pushbutton_text(False)

    def connect_device_open_close_slots(self, connection_dialog):
        connection_dialog.sig_opened.connect(self.slot_device_opened)
        connection_dialog.sig_closed.connect(self.slot_device_closed)

    def setup_connections(self):
        self.pgain_left_dblspinbox.valueChanged.connect(self.on_pgain_left_value_changed)
        self.pgain_right_dblspinbox.valueChanged.connect(self.on_pgain_right_value_changed)
        self.igain_left_dblspinbox.valueChanged.connect(self.on_igain_left_value_changed)
        self.igain_right_dblspinbox.valueChanged.connect(self.on_igain_right_value_changed)
        self.dgain_left_dblspinbox.valueChanged.connect(self.on_dgain_left_value_changed)
        self.dgain_right_dblspinbox.valueChanged.connect(self.on_dgain_right_value_changed)
        self.offset_left_dblspinbox.valueChanged.connect(self.on_offset_left_value_changed)
        self.offset_right_dblspinbox.valueChanged.connect(self.on_offset_right_value_changed)
        self.setpoint_left_dblspinbox.valueChanged.connect(self.on_setpoint_left_value_changed)
        self.setpoint_right_dblspinbox.valueChanged.connect(self.on_setpoint_right_value_changed)
        self.enable_disable_pushbutton.clicked.connect(self.on_enable_disable_pushbutton_clicked)

    def set_enable_disable_pushbutton_text(self, ctrl_enabled):
        if ctrl_enabled:
            self.enable_disable_pushbutton.setText(self.TEXT_ENABLED)
        else:
            self.enable_disable_pushbutton.setText(self.TEXT_DISABLED)

    @QtCore.Slot(PupaeThermalDevice,str)
    def slot_device_opened(self, device, port_name):
        self.device = device
        values = self.device.get_all()
        self.pgain_right, self.pgain_left = values['ctrl_pgain']
        self.igain_right, self.igain_left = values['ctrl_igain']
        self.dgain_right, self.dgain_left = values['ctrl_dgain']
        self.offset_right, self.offset_left = values['ctrl_offset']
        self.setpoint_right, self.setpoint_left = values['ctrl_setpoint']
        self.set_enable_disable_pushbutton_text(values['ctrl_enabled'])

    @QtCore.Slot()
    def slot_device_closed(self):
        self.device = None

    @property
    def pgain_left(self):
        return self.pgain_left_dblspinbox.value()

    @pgain_left.setter
    def pgain_left(self, value):
        self.pgain_left_dblspinbox.setValue(value)

    @property
    def pgain_right(self):
        return self.pgain_right_dblspinbox.value()

    @pgain_right.setter
    def pgain_right(self, value):
        self.pgain_right_dblspinbox.setValue(value)

    @property
    def igain_left(self):
        return self.igain_left_dblspinbox.value()

    @igain_left.setter
    def igain_left(self, value):
        self.igain_left_dblspinbox.setValue(value)

    @property
    def igain_right(self):
        return self.igain_right_dblspinbox.value()

    @igain_right.setter
    def igain_right(self, value):
        self.igain_right_dblspinbox.setValue(value)

    @property
    def dgain_left(self):
        return self.dgain_left_dblspinbox.value()

    @dgain_left.setter
    def dgain_left(self, value):
        self.dgain_left_dblspinbox.setValue(value)

    @property
    def dgain_right(self):
        return self.dgain_right_dblspinbox.value()

    @dgain_right.setter
    def dgain_right(self, value):
        self.dgain_right_dblspinbox.setValue(value)

    @property
    def offset_left(self):
        return self.offset_left_dblspinbox.value()

    @offset_left.setter
    def offset_left(self, value):
        self.offset_left_dblspinbox.setValue(value)

    @property
    def offset_right(self):
        return self.offset_right_dblspinbox.value()

    @offset_right.setter
    def offset_right(self, value):
        self.offset_right_dblspinbox.setValue(value)

    @property
    def setpoint_left(self):
        return self.setpoint_left_dblspinbox.value()

    @setpoint_left.setter
    def setpoint_left(self, value):
        if not self.setpoint_left_dblspinbox.hasFocus():
            self.setpoint_left_dblspinbox.setValue(value)

    @property
    def setpoint_right(self):
        return self.setpoint_right_dblspinbox.value()

    @setpoint_right.setter
    def setpoint_right(self, value):
        if not self.setpoint_right_dblspinbox.hasFocus():
            self.setpoint_right_dblspinbox.setValue(value)

    @property
    def setpoint(self):
        return self.setpoint_right, self.setpoint_left

    @setpoint.setter
    def setpoint(self, value):
        self.setpoint_right, self.setpoint_left = value

    def set_device_pgains(self):
        if self.device is not None:
            pgain_left = self.pgain_left_dblspinbox.value()
            pgain_right = self.pgain_right_dblspinbox.value()
            pgain_values = [pgain_right, pgain_left]
            self.device.set_ctrl_pgain(pgain_values)

    def set_device_igains(self):
        if self.device is not None:
            igain_left = self.igain_left_dblspinbox.value()
            igain_right = self.igain_right_dblspinbox.value()
            igain_values = [igain_right, igain_left]
            self.device.set_ctrl_igain(igain_values)

    def set_device_dgains(self):
        if self.device is not None:
            dgain_left = self.dgain_left_dblspinbox.value()
            dgain_right = self.dgain_right_dblspinbox.value()
            dgain_values = [dgain_right, dgain_left]
            self.device.set_ctrl_dgain(dgain_values)

    def set_device_offsets(self):
        if self.device is not None:
            offset_left = self.offset_left_dblspinbox.value()
            offset_right = self.offset_right_dblspinbox.value()
            offset_values = [offset_right, offset_left]
            self.device.set_ctrl_offset(offset_values)

    def set_device_setpoints(self):
        if self.device is not None:
            setpoint_left = self.setpoint_left_dblspinbox.value()
            setpoint_right = self.setpoint_right_dblspinbox.value()
            setpoint_values = [setpoint_right, setpoint_left]
            self.device.set_ctrl_setpoint(setpoint_values)

    def on_pgain_left_value_changed(self, new_value):
        self.set_device_pgains()

    def on_pgain_right_value_changed(self, new_value):
        self.set_device_pgains()

    def on_igain_left_value_changed(self, new_value):
        self.set_device_igains()

    def on_igain_right_value_changed(self, new_value):
        self.set_device_igains()

    def on_dgain_left_value_changed(self, new_value):
        self.set_device_dgains()

    def on_dgain_right_value_changed(self, new_value):
        self.set_device_dgains()

    def on_offset_left_value_changed(self, new_value):
        self.set_device_offsets()

    def on_offset_right_value_changed(self, new_value):
        self.set_device_offsets()

    def on_setpoint_left_value_changed(self, new_value):
        self.set_device_setpoints()
        self.sig_setpoint_left_changed.emit(new_value)

    def on_setpoint_right_value_changed(self, new_value):
        self.set_device_setpoints()
        self.sig_setpoint_right_changed.emit(new_value)

    def on_enable_disable_pushbutton_clicked(self):
        enabled = not self.device.get_ctrl_enabled()
        self.device.set_ctrl_enabled(enabled)
        self.set_enable_disable_pushbutton_text(enabled)

