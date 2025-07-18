#ifndef PUPAE_THERMAL_DEVICE_H
#define PUPAE_THERMAL_DEVICE_H
#include <Wire.h>
#include <Streaming.h>
#include <SparkFun_STTS22H.h>
#include <Adafruit_MotorShield.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>
#include <avdweb_Switch.h>

#include "constants.h"
#include "temperature_controller.h"

class PupaeThermalDevice {

    public:

        PupaeThermalDevice();
        void initialize();
        void update();

    protected:

        TemperatureController temperature_controller_[NUM_CONTROLLER];
        Adafruit_MotorShield motor_shield_ = Adafruit_MotorShield();
        Adafruit_SH1107 display_ = Adafruit_SH1107(DISPLAY_WIDTH, DISPLAY_HEIGHT, &Wire); 
        Switch r_setp_button_ = Switch(9);
        Switch l_setp_button_ = Switch(6);
        Switch enable_button_ = Switch(5);
        bool enabled_ = false;
};

#endif
