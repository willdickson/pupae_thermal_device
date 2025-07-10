#include "pupae_thermal_device.h"

PupaeThermalDevice::PupaeThermalDevice() {}

void PupaeThermalDevice::initialize() {
    Wire.begin();
    Serial.begin(SERIAL_BAUDRATE);
    motor_shield_.begin();
}

void PupaeThermalDevice::update() {
}
