from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from . import constants

class MplCanvas(FigureCanvas):

    NUM_COL = 2
    NUM_ROW = 2

    def __init__(self, parent=None, width=5, height=4, dpi=100):


        self.fig = Figure(figsize=(width, height), dpi=dpi)

        ax_temp_0 = self.fig.add_subplot(2,2,1)
        ax_temp_1 = self.fig.add_subplot(2,2,2, sharex=ax_temp_0, sharey=ax_temp_0)
        ax_powr_0 = self.fig.add_subplot(2,2,3, sharex=ax_temp_0)
        ax_powr_1 = self.fig.add_subplot(2,2,4, sharex=ax_temp_0, sharey=ax_powr_0)
        self.ax_temp = (ax_temp_0, ax_temp_1)
        self.ax_powr = (ax_powr_0, ax_powr_1)
        self.ax = (*self.ax_temp, *self.ax_powr)
        self.set_grid(True)

        # Create setpoint line
        temp_mid = 0.5*(constants.PLOT_TEMPERATURE_MIN + constants.PLOT_TEMPERATURE_MAX)
        line_setp_0, = self.ax_temp[0].plot([0,1],[temp_mid, temp_mid],'k')
        line_setp_1, = self.ax_temp[1].plot([0,1],[temp_mid, temp_mid],'k')
        self.line_setp = (line_setp_0, line_setp_1)

        self.set_plot_temperature_range(
                constants.PLOT_TEMPERATURE_MIN, 
                constants.PLOT_TEMPERATURE_MAX,
                )

        self.set_plot_power_range(
                constants.PLOT_POWER_MIN, 
                constants.PLOT_POWER_MAX,
                )

        self.ax_temp[0].set_ylabel('temperature (C)')

        self.ax_powr[0].set_ylabel('power')
        self.ax_temp[0].tick_params(labelbottom=False)
        self.ax_temp[1].tick_params(labelbottom=False)
        self.ax_temp[1].tick_params(labelleft=False)
        self.ax_powr[1].tick_params(labelleft=False)
        self.ax_powr[0].set_xlabel('t (s)')
        self.ax_powr[1].set_xlabel('t (s)')


        super().__init__(self.fig)

    def set_grid(self, value):
        for ax in self.ax:
            ax.grid(value)

    def set_plot_time_window(self, value):
        self.ax_temp[0].set_xlim(0, value)
        self.adjust_setpoint_lines()

    def set_plot_temperature_range(self, min_value, max_value):
        self.ax_temp[0].set_ylim(min_value, max_value)

    def set_plot_power_range(self, min_value, max_value):
        self.ax_powr[0].set_ylim(min_value, max_value)

    def set_setpoint_right(self, value):
        self.line_setp[1].set_ydata([value,value])

    def set_setpoint_left(self, value):
        self.line_setp[0].set_ydata([value,value])

    def adjust_setpoint_lines(self):
        xlim = self.ax_temp[0].get_xlim()
        for line in self.line_setp:
            line.set_xdata(xlim)











        
