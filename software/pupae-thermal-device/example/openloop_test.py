import time
import numpy as np
from pupae_thermal_device import PupaeThermalDevice

port = '/dev/ttyACM0'
duration = 2*60.0 
dt = 0.25
offset = 20 
filename = f'data_offset_{int(offset)}.txt'

print(f'running openloop test')
print(f' duration: {duration}')
print(f' offset:   {offset}') 
print(f' dt:       {dt}')
print(f' filename: {filename}')
print()
time.sleep(1.0)


dev = PupaeThermalDevice(port)

# Store pgains and igains for restoring later
pgain_bak = dev.get_ctrl_pgain()
igain_bak = dev.get_ctrl_igain()
dev.set_ctrl_pgain([0,0])
dev.set_ctrl_igain([0,0])
dev.set_ctrl_offset([-offset, offset])
dev.set_ctrl_enabled(True)

t_start = time.time()
t_now = 0.0
time_list = []
temp_list = []

done = False

while t_now < duration:
    t_now = time.time() - t_start
    temp = dev.get_temperature()
    print(f't: {t_now}, temp: {temp}')
    time_list.append(t_now)
    temp_list.append(temp)
    time.sleep(dt)


data = np.zeros((len(time_list), 3))

data[:,0] = np.array(time_list)
data[:,1] = np.array([x for x,_ in temp_list])
data[:,2] = np.array([y for _,y in temp_list])

np.savetxt(filename, data)
print(f'data saved to: {filename}')

dev.set_ctrl_enabled(False)
dev.set_ctrl_pgain(pgain_bak)
dev.set_ctrl_igain(igain_bak)
dev.set_ctrl_offset([0,0])



