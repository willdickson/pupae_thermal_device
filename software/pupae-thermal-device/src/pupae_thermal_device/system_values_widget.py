from PySide6 import QtWidgets
from .ui_system_values_widget import Ui_SystemValuesWidget


class SystemValuesWidget(QtWidgets.QWidget, Ui_SystemValuesWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initialize()
        self.setup_connections()

    def initialize(self):
        pass

    def setup_connections(self):
        pass
