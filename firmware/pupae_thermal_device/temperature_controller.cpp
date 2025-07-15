#include "temperature_controller.h"
#include <Streaming.h>

TemperatureController::TemperatureController() {}


void TemperatureController::initialize(uint8_t sensor_address, Adafruit_DCMotor *motor) {
    Serial << "setting up temperature sensor" << endl;
    sensor_address_ = sensor_address;
    while (!sensor_.begin(sensor_address_)) { 
        Serial << "  temperature sensor failed to begin" << endl; 
        delay(SENSOR_SETUP_DT); 
    }
    sensor_.setDataRate(STTS22H_POWER_DOWN);
    delay(SENSOR_SETUP_DT);
    sensor_.setDataRate(STTS22H_25Hz);
    sensor_.enableAutoIncrement();
    delay(SENSOR_SETUP_DT);
    Serial << "temperature sensor ready" << endl;

    peltier_drive_.initialize(motor);
}


void TemperatureController::update() {
    if (enabled_) {
        sensor_.getTemperatureC(&temperature_);
        float error = setpoint_ - temperature_;
        float delta = setpoint_ - ambient_;
        float power = gain_*error + ff_slope_*delta;
        //Serial << "power: " << power << endl;
        peltier_drive_.set_power(power);
    }
    else {
        peltier_drive_.set_power(0.0);
    }
}


void TemperatureController::update(float ambient) {
    set_ambient(ambient);
    update();
}


float TemperatureController::temperature() {
    return temperature_;
}


uint8_t TemperatureController::sensor_address() {
    return sensor_address_;
}


bool TemperatureController::enabled() {
    return enabled_;
}


void TemperatureController::set_enabled(bool value) {
    enabled_ = value;
    if (!enabled_) {
        peltier_drive_.set_power(0.0);
    }
}


float TemperatureController::setpoint() {
    return setpoint_;
}


void TemperatureController::set_setpoint(float value) {
    setpoint_ = value;
}


float TemperatureController::gain() {
    return gain_;
}


void TemperatureController::set_gain(float value) {
    gain_ = value;
}


float TemperatureController::ff_slope() {
    return ff_slope_;
}


void TemperatureController::set_ff_slope(float value) {
    ff_slope_ = value;
}


float TemperatureController::ambient() {
    return ambient_;
}


void TemperatureController::set_ambient(float value) {
    ambient_ = value;
}

