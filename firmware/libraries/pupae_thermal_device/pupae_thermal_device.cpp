#include "pupae_thermal_device.h"
#include <Streaming.h>

PupaeThermalDevice::PupaeThermalDevice() {}

void PupaeThermalDevice::initialize() {
    Wire.begin();
    Serial.begin(SERIAL_BAUDRATE);
    motor_shield_.begin();

    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        Adafruit_DCMotor *motor = motor_shield_.getMotor(DRIVE_MOTOR_NUMBER[i]);
        temperature_controller_[i].initialize(SENSOR_ADDRESS[i], motor);
    }

    temperature_controller_[0].set_setpoint(22.0);
    temperature_controller_[1].set_setpoint(22.0);

    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        temperature_controller_[i].set_enabled(true);
        temperature_controller_[i].set_pgain(100.0);
        temperature_controller_[i].set_igain(0.005);
    }

}

void PupaeThermalDevice::update() {

    for (uint8_t i=0; i<NUM_CONTROLLER; i++) { 
        temperature_controller_[i].update();
        float temp = temperature_controller_[i].temperature();
        float setp = temperature_controller_[i].setpoint();
        float err  = temperature_controller_[i].error();
        float ierr = temperature_controller_[i].ierror();
        float power = temperature_controller_[i].power();
        Serial << i;  
        Serial << ", temp: " << temp; 
        Serial << ", setp: " << setp; 
        Serial << ", err: "  << err; 
        Serial << ", ierr: " << ierr; 
        Serial << ", power: " << power; 
        Serial << endl; 
    }
    Serial << endl;
    delay(LOOP_DT);
}
