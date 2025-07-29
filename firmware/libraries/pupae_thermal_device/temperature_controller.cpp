#include "temperature_controller.h"
#include <Streaming.h>

TemperatureController::TemperatureController() {}


void TemperatureController::initialize(uint8_t sensor_address, Adafruit_DCMotor *motor) {
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

    peltier_drive_.initialize(motor);
}


void TemperatureController::update() {
    sensor_.getTemperatureC(&temperature_);
    if (enabled_) {
        error_ = setpoint_ - temperature_;
        ierror_ = ierror_ + error_;
        ierror_ = constrain(ierror_, -1.0*DRIVE_MAX_POWER/igain_, 1.0*DRIVE_MAX_POWER/igain_);
        power_ = pgain_*error_ + igain_*ierror_ + offset_;
        peltier_drive_.set_power(power_);
    }
    else {
        peltier_drive_.set_power(0.0);
    }
}


float TemperatureController::temperature() {
    return temperature_;
}


float TemperatureController::power() {
    return power_;
}


float TemperatureController::error() {
    return error_;
}


float TemperatureController::ierror() {
    return ierror_;
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
        ierror_ = 0.0;
    }
}


float TemperatureController::setpoint() {
    return setpoint_;
}


void TemperatureController::set_setpoint(float value) {
    setpoint_ = value;
}


float TemperatureController::pgain() {
    return pgain_;
}


void TemperatureController::set_pgain(float value) {
    pgain_ = fabs(value);
}


float TemperatureController::igain() {
    return igain_;
}


void TemperatureController::set_igain(float value) {
    igain_ = fabs(value);
}


float TemperatureController::offset() {
    return offset_;
}


void TemperatureController::set_offset(float value) {
    offset_ = value;
}


