import sys
from PySide6 import QtWidgets
from .pupae_thermal_device_tuner import TunerMainWindow

def tuner_app_main():
    app = QtWidgets.QApplication(sys.argv)
    window = TunerMainWindow()
    window.show()
    app.exec()


