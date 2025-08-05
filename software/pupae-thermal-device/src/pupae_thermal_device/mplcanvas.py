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
        ax_power_0 = self.fig.add_subplot(2,2,3, sharex=ax_temp_0)
        ax_power_1 = self.fig.add_subplot(2,2,4, sharex=ax_temp_0, sharey=ax_power_0)
        self.ax_temp = (ax_temp_0, ax_temp_1)
        self.ax_power = (ax_power_0, ax_power_1)
        self.ax = (*self.ax_temp, *self.ax_power)
        self.ax_temp[0].set_ylabel('temperature (C)')
        self.ax_power[0].set_ylabel('power')
        self.ax_temp[0].tick_params(labelbottom=False)
        self.ax_temp[1].tick_params(labelbottom=False)
        self.ax_temp[1].tick_params(labelleft=False)
        self.ax_power[1].tick_params(labelleft=False)
        self.ax_power[0].set_xlabel('t (s)')
        self.ax_power[1].set_xlabel('t (s)')
        self.ax_temp[0].set_title('Left')
        self.ax_temp[1].set_title('Right')
        self.set_grid(True)

        # Create setpoint line
        line_setp_0, = self.ax_temp[0].plot([0],[0],'k')
        line_setp_1, = self.ax_temp[1].plot([0],[0],'k')
        self.line_setp = line_setp_0, line_setp_1

        # Create temperature line
        line_temp_0, = self.ax_temp[0].plot([0],[0],'b')
        line_temp_1, = self.ax_temp[1].plot([0],[0],'b')
        self.line_temp = line_temp_0, line_temp_1

        # Create error line
        line_error_0, = self.ax_power[0].plot([0],[0],'b')
        line_error_1, = self.ax_power[1].plot([0],[0],'b')
        self.line_error = line_error_0, line_error_1

        # Create ierror line
        line_ierror_0, = self.ax_power[0].plot([0],[0],'g')
        line_ierror_1, = self.ax_power[1].plot([0],[0],'g')
        self.line_ierror = line_ierror_0, line_ierror_1

        # Create power line
        line_power_0, = self.ax_power[0].plot([0],[0],'r')
        line_power_1, = self.ax_power[1].plot([0],[0],'r')
        self.line_power = line_power_0, line_power_1

        # Set temperature plot legends
        self.ax_temp[0].legend(
                (line_setp_0, line_temp_0), 
                ('setpoint', 'plate'), 
                loc='upper right', 
                )
        self.ax_temp[1].legend(
                (line_setp_1, line_temp_1), 
                ('setpoint', 'plate'), 
                loc='upper right', 
                )

        # Set power plot legends
        self.ax_power[0].legend(
                (line_error_0, line_ierror_0, line_power_0), 
                ('error', 'ierror', 'power'), 
                loc='upper right', 
                )
        self.ax_power[1].legend(
                (line_error_1, line_ierror_1, line_power_1), 
                ('error', 'ierror', 'power'), 
                loc='upper right', 
                )

        # Set axis ranges
        self.set_plot_temperature_range(
                constants.PLOT_TEMPERATURE_MIN, 
                constants.PLOT_TEMPERATURE_MAX,
                )

        self.set_plot_power_range(
                constants.PLOT_POWER_MIN, 
                constants.PLOT_POWER_MAX,
                )

        super().__init__(self.fig)

    def set_grid(self, value):
        for ax in self.ax:
            ax.grid(value)

    def set_plot_time_window(self, value):
        self.ax_temp[0].set_xlim(0, value)
        #self.adjust_setpoint_lines()

    def set_plot_temperature_range(self, min_value, max_value):
        self.ax_temp[0].set_ylim(min_value, max_value)

    def set_plot_power_range(self, min_value, max_value):
        self.ax_power[0].set_ylim(min_value, max_value)

    def set_setpoint_right(self, value):
        self.line_setp[1].set_ydata([value,value])

    def set_setpoint_left(self, value):
        self.line_setp[0].set_ydata([value,value])

    def update_plot_lines(self, plot_data):
        t = plot_data['t']
        self.update_setpoint_lines(t, plot_data['setpoint'])
        self.update_temperature_lines(t, plot_data['temperature'])
        self.update_error_lines(t, plot_data['error'])
        self.update_ierror_lines(t, plot_data['ierror'])
        self.update_power_lines(t, plot_data['power'])

    def update_setpoint_lines(self, t, setpoint_data):
        self.line_setp[0].set_data(t, setpoint_data['left'])
        self.line_setp[1].set_data(t, setpoint_data['right'])

    def update_temperature_lines(self, t, temperature_data):
        self.line_temp[0].set_data(t, temperature_data['left'])
        self.line_temp[1].set_data(t, temperature_data['right'])
        
    def update_error_lines(self, t, error_data):
        self.line_error[0].set_data(t, error_data['left'])
        self.line_error[1].set_data(t, error_data['right'])

    def update_ierror_lines(self, t, ierror_data):
        self.line_ierror[0].set_data(t, ierror_data['left'])
        self.line_ierror[1].set_data(t, ierror_data['right'])

    def update_power_lines(self, t, power_data):
        self.line_power[0].set_data(t, power_data['left'])
        self.line_power[1].set_data(t, power_data['right'])











        
