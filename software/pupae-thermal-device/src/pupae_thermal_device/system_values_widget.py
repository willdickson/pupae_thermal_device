from PySide6 import QtWidgets
from .ui_system_values_widget import Ui_SystemValuesWidget


class SystemValuesWidget(QtWidgets.QWidget, Ui_SystemValuesWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    def set_values(self, values):
        self.set_temperature(values['temperature'])
        self.set_error(values['ctrl_error'])
        self.set_ierror(values['ctrl_ierror'])
        self.set_power(values['ctrl_power'])

    def set_temperature(self, temperature):
        temperature_right, temperature_left = temperature
        self.set_temperature_right(temperature_right)
        self.set_temperature_left(temperature_left)

    def set_error(self, error):
        error_right, error_left = error
        self.set_error_right(error_right)
        self.set_error_left(error_left)

    def set_ierror(self, ierror):
        ierror_right, ierror_left = ierror
        self.set_ierror_right(ierror_right)
        self.set_ierror_left(ierror_left)

    def set_power(self, power):
        power_right, power_left = power
        self.set_power_right(power_right)
        self.set_power_left(power_left)

    def set_temperature_right(self, value):
        self.temperature_right_value_label.setText(f'{value:.1f}')

    def set_temperature_left(self, value):
        self.temperature_left_value_label.setText(f'{value:.1f}')

    def set_error_right(self, value):
        self.error_right_value_label.setText(f'{value:.1f}')

    def set_error_left(self, value):
        self.error_left_value_label.setText(f'{value:.1f}')

    def set_ierror_right(self, value):
        self.ierror_right_value_label.setText(f'{value:.1f}')

    def set_ierror_left(self, value):
        self.ierror_left_value_label.setText(f'{value:.1f}')

    def set_power_right(self, value):
        self.power_right_value_label.setText(f'{value:.1f}')

    def set_power_left(self, value):
        self.power_left_value_label.setText(f'{value:.1f}')
