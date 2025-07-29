import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

filename = sys.argv[1]

data = load_data(filename)

t      = data['t']
pgain  = data['pgain']
igain  = data['igain']
temp   = data['temperature']
error  = data['ctrl_error']
ierror = data['ctrl_ierror']
power  = data['ctrl_power']
setpoint = data['setpoint']


for i in range(2):

    fig, ax = plt.subplots(2,1, sharex=True)
    
    ax[0].plot([t[0], t[-1]], [setpoint[i], setpoint[i]], 'k', label='setp')
    ax[0].plot(t, temp[:,i],'b', label='temp')
    ax[0].set_ylabel('Temp (C)')
    ax[0].grid(True)
    ax[0].set_title(f'controller #{i}')
    ax[0].legend(loc='upper right')
    
    ax[1].plot(t[1:], pgain*error[1:,i],'b', label='error')
    ax[1].plot(t[1:], igain*ierror[1:,i],'g', label='ierro')
    ax[1].plot(t[1:], power[1:,i], 'r', label='power')
    ax[1].set_ylabel('power')
    ax[1].set_xlabel('t (sec)')
    ax[1].grid(True)
    ax[1].legend(loc='upper right')


plt.show()
