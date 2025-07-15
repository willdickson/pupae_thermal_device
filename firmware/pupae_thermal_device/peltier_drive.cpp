#include "peltier_drive.h"
#include <cmath>
#include <Streaming.h>

PeltierDrive::PeltierDrive() { }


void PeltierDrive::initialize(Adafruit_DCMotor *motor) {
    motor_ = motor; 
}

float PeltierDrive::power() {
    return power_;
}

void PeltierDrive::set_power(float value) {
    uint16_t speed = uint16_t(0.01*MAX_MOTOR_SPEED*fabs(value)); 
    //Serial << "speed: " << speed << endl;
    motor_ -> setSpeedFine(speed);
    if (power_ < 0) {
        motor_ -> run(FORWARD);   // Cooling 
    }
    else {
        motor_ -> run(BACKWARD);  // Heating
    }
    power_ = value;
}
