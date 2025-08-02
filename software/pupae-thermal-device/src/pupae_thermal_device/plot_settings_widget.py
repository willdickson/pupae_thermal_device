from PySide6 import QtCore
from PySide6 import QtWidgets
from .ui_plot_settings_widget import Ui_PlotSettingsWidget


class PlotSettingsWidget(QtWidgets.QWidget, Ui_PlotSettingsWidget):

    sig_plot_window_changed = QtCore.Signal(float)
    sig_plot_window_reset = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.plot_window_dblspinbox.valueChanged.connect(self.on_plot_window_value_changed)
        self.plot_reset_pushbutton.clicked.connect(self.on_plot_reset_pushbutton_clicked)

    @property
    def window(self):
        return self.plot_window_dblspinbox.value()

    @window.setter
    def window(self,value):
        self.plot_window_dblspinbox.setValue(value)


    def on_plot_window_value_changed(self, new_value):
        self.sig_plot_window_changed.emit(new_value)

    def on_plot_reset_pushbutton_clicked(self):
        self.sig_plot_window_reset()

