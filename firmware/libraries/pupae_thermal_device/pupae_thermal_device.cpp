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
        temperature_controller_[i].set_enabled(enabled_);
        temperature_controller_[i].set_setpoint(DEFAULT_SETP[i]);
    }

    display_.begin(DISPLAY_ADDRESS, true);
    display_.setRotation(1);
    display_.clearDisplay();
    display_.setTextSize(1);
    display_.setTextColor(SH110X_WHITE);

}

void PupaeThermalDevice::update() {
    handle_button_input();
    update_timed_services();
}

void PupaeThermalDevice::update_timed_services() {
    unsigned long now = millis();
    unsigned long dt = now - t_last_update_;
    if (dt >= LOOP_DT) {
        update_controllers();
        update_display();
        t_last_update_ = now;
    }
}

void PupaeThermalDevice::update_controllers() { 
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) { 
        temperature_controller_[i].update();
    }
}


void PupaeThermalDevice::handle_button_input() {

    // Check for setpoint update
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        setpoint_button_[i].poll();
        if (setpoint_button_[i].step_indicated()) {
            float step = setpoint_button_[i].step();
            float old_setpoint = temperature_controller_[i].setpoint();
            float new_setpoint = old_setpoint + step; 
            new_setpoint = constrain(new_setpoint, MIN_SETP_TEMP_C, MAX_SETP_TEMP_C);
            temperature_controller_[i].set_setpoint(new_setpoint);
        }
    }

    // Check for change in enable/disable
    enable_button_.poll();
    if (enable_button_.pushed()) {
        enabled_ = !enabled_;
        for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
            temperature_controller_[i].set_enabled(enabled_);
        }
    }
}


void PupaeThermalDevice::update_display() {
    display_.clearDisplay();
    display_.setCursor(0, 0);
    display_.printf("SIDE  SETP   TEMP (C)");

    uint8_t row_step = 16;
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) { 
        float temp = temperature_controller_[i].temperature();
        float setp = temperature_controller_[i].setpoint();
        display_.setCursor(0, (i+1)*row_step);
        display_.printf("  %c    %3.1f   %3.1f", SENSOR_SIDE_LABEL[i], setp, temp);
    }
    display_.setCursor(0, 3*row_step);
    if (enabled_) {
        display_.printf("  ENABLED");                  
    } 
    else {
        display_.printf("  DISABLED");                  
    }
    display_.display();
}
