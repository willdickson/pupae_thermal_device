#ifndef PELTIER_DRIVE_H
#define PELTIER_DRIVE_H
#include "Adafruit_MotorShield.h"

class PeltierDrive {


    public:
        PeltierDrive();
        void initialize(Adafruit_DCMotor *motor);

        float power();
        void set_power(float power);

        const static uint16_t MAX_MOTOR_SPEED = (2<<11)-1;

    protected:
        Adafruit_DCMotor *motor_ = nullptr; 
        float power_ = 0.0;

};

#endif
