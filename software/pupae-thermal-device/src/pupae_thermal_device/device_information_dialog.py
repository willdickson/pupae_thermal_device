from PySide6 import QtCore
from PySide6 import QtWidgets
from .ui_device_information_dialog import Ui_DeviceInformationDialog

class DeviceInformationDialog(Ui_DeviceInformationDialog, QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    @property
    def hardware_version(self):
        return self.hardware_version_value_label.text()

    @hardware_version.setter
    def hardware_version(self, value):
        self.hardware_version_value_label.setText(value)

    @property
    def firmware_version(self):
        return self.firmware_version_value_label.text()

    @firmware_version.setter
    def firmware_version(self, value):
        self.firmware_version_value_label.setText(value)




