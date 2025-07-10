#ifndef PELTIER_DRIVE_H
#define PELTIER_DRIVE_H
#include "Adafruit_MotorShield.h"

class PeltierDrive {

    public:
        PeltierDrive();
        void initialize(Adafruit_DCMotor *motor);

        float power();
        void set_power(float value);

    protected:
        uint8_t drive_number_ = 0;
        float power_ = 0.0;
        Adafruit_DCMotor *motor_ = nullptr; 

};

#endif
