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
        temperature_controller_[i].set_enabled(enabled_);
        temperature_controller_[i].set_pgain(100.0);
        temperature_controller_[i].set_igain(0.005);
    }

    display_.begin(DISPLAY_ADDRESS, true);
    display_.setRotation(1);
    display_.clearDisplay();
    display_.display();
    delay(2000);
    display_.clearDisplay();
    display_.setTextSize(1);
    display_.setTextColor(SH110X_WHITE);

}

void PupaeThermalDevice::update() {

    r_setp_button_.poll();
    if (r_setp_button_.pushed()) {
        Serial << "R setp button" << endl;
    }

    l_setp_button_.poll();
    if(l_setp_button_.pushed()) {
        Serial << "L setp button" << endl;
    }

    enable_button_.poll();
    if (enable_button_.pushed()) {
        enabled_ = !enabled_;
        for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
            temperature_controller_[i].set_enabled(enabled_);
        }
    }

    display_.clearDisplay();
    display_.setCursor(0, 0);
    display_.printf("SIDE  SETP   TEMP (C)");

    uint8_t step = 16;
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) { 
        temperature_controller_[i].update();
        float temp = temperature_controller_[i].temperature();
        float setp = temperature_controller_[i].setpoint();
        float err  = temperature_controller_[i].error();
        float ierr = temperature_controller_[i].ierror();
        float power = temperature_controller_[i].power();
        //Serial << i;  
        //Serial << ", temp: " << temp; 
        //Serial << ", setp: " << setp; 
        //Serial << ", err: "  << err; 
        //Serial << ", ierr: " << ierr; 
        //Serial << ", power: " << power; 
        //Serial << endl; 
        display_.setCursor(0, (i+1)*step);
        display_.printf("  %c   %4.2f  %4.2f", SENSOR_SIDE_LABEL[i], setp, temp);
    }
    display_.setCursor(0, 3*step);
    if (enabled_) {
        display_.printf("  ENABLED");                  
    } 
    else {
        display_.printf("  DISABLED");                  
    }
    display_.display();
    delay(LOOP_DT);
}
