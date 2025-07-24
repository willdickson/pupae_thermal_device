from pupae_thermal_device import PupaeThermalDevice

port = '/dev/ttyACM0'

dev = PupaeThermalDevice(port)

temperature = dev.get_temperature()
ctrl_power = dev.get_ctrl_power()
ctrl_error = dev.get_ctrl_error()
ctrl_ierror = dev.get_ctrl_ierror()
ctrl_pgain = dev.get_ctrl_pgain()
ctrl_igain = dev.get_ctrl_igain()
ctrl_setpoint = dev.get_ctrl_setpoint()
ctrl_enabled = dev.get_ctrl_enabled()

print(f'temperature:    {temperature}')
print(f'ctrl_power:     {ctrl_power}')
print(f'ctrl_error:     {ctrl_error}')
print(f'ctrl_ierror:    {ctrl_ierror}')
print(f'ctrl_pgain:     {ctrl_pgain}')
print(f'ctrl_igain:     {ctrl_igain}')
print(f'ctrl_setpoint:  {ctrl_setpoint}')
print(f'ctrl_enabled:   {ctrl_enabled}')
print()

value_dict = dev.get_all()
for k,v in value_dict.items():
    print(f'{k}: {v}')

