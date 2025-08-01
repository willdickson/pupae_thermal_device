from PySide6 import QtWidgets
from .ui_status_info import Ui_StatusInfo

class StatusInfo(QtWidgets.QWidget, Ui_StatusInfo):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    def set_text(self, text):
        self.status_label.setText(text)

