import time
import pickle
import numpy as np
from pupae_thermal_device import PupaeThermalDevice

port = '/dev/ttyACM0'
duration = 3*60 
dt = 0.25
pgain = 40
igain = 0.02
setpoint = [18, 32]
filename = f'closedloop_data_p{int(pgain):03d}_i{int(1000*igain):03d}.pkl'

print(f'running openloop test')
print(f' duration: {duration}')
print(f' dt:       {dt}')
print(f' pgain:    {pgain}')
print(f' igain:    {igain}')
print(f' setpoint  {setpoint}')
print(f' filename: {filename}')
print()
time.sleep(1.0)


dev = PupaeThermalDevice(port)

# Store pgains and igains for restoring later
pgain_bak = dev.get_ctrl_pgain()
igain_bak = dev.get_ctrl_igain()
dev.set_ctrl_pgain([pgain,pgain])
dev.set_ctrl_igain([igain,igain])
dev.set_ctrl_offset([0,0])
dev.set_ctrl_enabled(True)

t_start = time.time()
t_now = 0.0

time_list = []
temp_list = []
error_list = []
ierror_list = []
power_list = []

done = False

while t_now < duration:
    t_now = time.time() - t_start
    data = dev.get_all()
    temp = data['temperature']

    print(f't: {t_now}, temp: {temp}')
    time_list.append(t_now)
    temp_list.append(data['temperature'])
    error_list.append(data['ctrl_error'])
    ierror_list.append(data['ctrl_ierror'])
    power_list.append(data['ctrl_power'])
    time.sleep(dt)



data = {}
data['t'] = np.array(time_list)
data['pgain'] = pgain
data['igain'] = igain
data['setpoint'] = setpoint
data['temperature'] = np.array(temp_list)
data['ctrl_error'] = np.array(error_list)
data['ctrl_ierror'] = np.array(ierror_list)
data['ctrl_power'] = np.array(power_list)

with open(filename, 'wb') as f:
    pickle.dump(data, f)

print(f'data saved to: {filename}')

dev.set_ctrl_enabled(False)
dev.set_ctrl_pgain(pgain_bak)
dev.set_ctrl_igain(igain_bak)
dev.set_ctrl_offset([0,0])
