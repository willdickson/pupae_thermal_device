import time
from pupae_thermal_device import PupaeThermalDevice

port = '/dev/ttyACM0'

dev = PupaeThermalDevice(port)

temperature = dev.get_temperature()
ctrl_power = dev.get_ctrl_power()
ctrl_error = dev.get_ctrl_error()
ctrl_ierror = dev.get_ctrl_ierror()
ctrl_derror = dev.get_ctrl_derror()
ctrl_pgain = dev.get_ctrl_pgain()
ctrl_igain = dev.get_ctrl_igain()
ctrl_dgain = dev.get_ctrl_dgain()
ctrl_offset = dev.get_ctrl_offset()
ctrl_setpoint = dev.get_ctrl_setpoint()
ctrl_enabled = dev.get_ctrl_enabled()

print(f'temperature:    {temperature}')
print(f'ctrl_power:     {ctrl_power}')
print(f'ctrl_error:     {ctrl_error}')
print(f'ctrl_ierror:    {ctrl_ierror}')
print(f'ctrl_derror:    {ctrl_derror}')
print(f'ctrl_pgain:     {ctrl_pgain}')
print(f'ctrl_igain:     {ctrl_igain}')
print(f'ctrl_dgain:     {ctrl_igain}')
print(f'ctrl_offset:    {ctrl_offset}')
print(f'ctrl_setpoint:  {ctrl_setpoint}')
print(f'ctrl_enabled:   {ctrl_enabled}')
print()

value_dict = dev.get_all()
for k,v in value_dict.items():
    print(f'{k}: {v}')
print()

if 0:
    print('enabling')
    rsp = dev.set_ctrl_enabled(True)
    print(rsp)
    time.sleep(5.0)
    print('disabling')
    rsp = dev.set_ctrl_enabled(False)
    print(rsp)
    print()


rsp = dev.set_ctrl_pgain([110,90])
ctrl_pgain = dev.get_ctrl_pgain()
print(f'rsp:            {rsp}')
print(f'ctrl_pgain:     {ctrl_pgain}')

rsp = dev.set_ctrl_pgain([100,100])
ctrl_pgain = dev.get_ctrl_pgain()
print(f'rsp:            {rsp}')
print(f'ctrl_pgain:     {ctrl_pgain}')
print()

rsp = dev.set_ctrl_igain([0.007,0.004])
ctrl_igain = dev.get_ctrl_igain()
print(f'rsp:            {rsp}')
print(f'ctrl_igain:     {ctrl_igain}')

rsp = dev.set_ctrl_igain([0.0,0.0])
ctrl_igain = dev.get_ctrl_igain()
print(f'rsp:            {rsp}')
print(f'ctrl_igain:     {ctrl_igain}')
print()

rsp = dev.set_ctrl_dgain([0.01,0.01])
ctrl_igain = dev.get_ctrl_dgain()
print(f'rsp:            {rsp}')
print(f'ctrl_dgain:     {ctrl_igain}')

rsp = dev.set_ctrl_dgain([0.0,0.0])
ctrl_igain = dev.get_ctrl_dgain()
print(f'rsp:            {rsp}')
print(f'ctrl_dgain:     {ctrl_igain}')
print()


rsp = dev.set_ctrl_setpoint([19,30])
ctrl_setpoint = dev.get_ctrl_setpoint()
print(f'rsp:            {rsp}')
print(f'ctrl_setpoint:  {ctrl_setpoint}')

rsp = dev.set_ctrl_setpoint([18,32])
ctrl_setpoint = dev.get_ctrl_setpoint()
print(f'rsp:            {rsp}')
print(f'ctrl_setpoint:  {ctrl_setpoint}')
