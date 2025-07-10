#ifndef PUPAE_THERMAL_DEVICE_H
#define PUPAE_THERMAL_DEVICE_H
#include <Wire.h>
#include <Streaming.h>
#include "SparkFun_STTS22H.h"
#include "Adafruit_MotorShield.h"
#include "constants.h"

class PupaeThermalDevice {

    public:

        PupaeThermalDevice();
        void initialize();
        void update();

    protected:

        Adafruit_MotorShield motor_shield_ = Adafruit_MotorShield();

};

#endif
