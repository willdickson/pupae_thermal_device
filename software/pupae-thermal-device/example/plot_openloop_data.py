import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]

data = np.loadtxt(filename)

t = data[:,0]
temp0 = data[:,1]
temp1 = data[:,2]

if 1:
    fig, ax = plt.subplots(1,1, sharex=True)
    
    ax.plot(t, temp0, 'b')
    ax.set_ylabel('Temp (C)')
    ax.grid(True)
    
    ax.plot(t, temp1, 'g')
    ax.set_ylabel('Temp (C)')
    ax.set_xlabel('t (sec)')
    ax.grid(True)


if 0:
    fig, ax = plt.subplots(2,1, sharex=True)
    
    ax[0].plot(t, temp0)
    ax[0].set_ylabel('Temp (C)')
    ax[0].grid(True)
    
    ax[1].plot(t, temp1)
    ax[1].set_ylabel('Temp (C)')
    ax[1].set_xlabel('t (sec)')
    ax[1].grid(True)

plt.show()
