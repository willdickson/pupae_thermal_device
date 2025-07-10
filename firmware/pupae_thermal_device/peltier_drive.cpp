#include <cmath>
#include "peltier_drive.h"

PeltierDrive::PeltierDrive() { }


void PeltierDrive::initialize(Adafruit_DCMotor *motor) {
    motor_ = motor; 
}

float PeltierDrive::power() {
    return power_;
}

void PeltierDrive::set_power(float value) {
    power_ = value;
    uint8_t power_int = uint8_t(constrain(255*uint32_t(fabs(power_)),0,255));
    uint
    if (power_ > 0) {


}
