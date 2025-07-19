#ifndef PUPAE_THERMAL_DEVICE_H
#define PUPAE_THERMAL_DEVICE_H
#include <Wire.h>
#include <Streaming.h>
#include <SparkFun_STTS22H.h>
#include <Adafruit_MotorShield.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>

#include "constants.h"
#include "button.h"
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

        StepButton r_setp_button_ = StepButton(R_SETP_BUTTON_PIN); 
        StepButton l_setp_button_ = StepButton(L_SETP_BUTTON_PIN);
        Button enable_button_ = Button(ENABLE_BUTTON_PIN);

        bool enabled_ = false;
        unsigned long t_last_update_= 0;

        void handle_button_input();
        void update_timed_services();
        void update_controllers();
        void update_display();

};

#endif
