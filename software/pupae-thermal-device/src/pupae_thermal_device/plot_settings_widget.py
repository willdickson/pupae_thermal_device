from PySide6 import QtWidgets
from .ui_plot_settings_widget import Ui_PlotSettingsWidget


class PlotSettingsWidget(QtWidgets.QWidget, Ui_PlotSettingsWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setup_connections()


    def setup_connections(self):
        self.plot_window_dblspinbox.valueChanged.connect(self.on_plot_window_value_changed)
        self.plot_reset_pushbutton.clicked.connect(self.on_plot_reset_pushbutton_clicked)


    def on_plot_window_value_changed(self, new_value):
        print(f'plot window: {new_value}')


    def on_plot_reset_pushbutton_clicked(self):
        print('plot reset')

