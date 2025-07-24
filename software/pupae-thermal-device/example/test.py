from pupae_thermal_device import PupaeThermalDevice

port = '/dev/ttyACM0'

dev = PupaeThermalDevice(port)
for i in range(100):
    vals = dev.get_temperature()
    print(vals)

