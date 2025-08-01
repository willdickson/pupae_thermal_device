#ifndef PUPAE_THERMAL_DEVICE_H
#define PUPAE_THERMAL_DEVICE_H
#include <map>
#include <functional>
#include <Wire.h>
#include <Streaming.h>
#include <SparkFun_STTS22H.h>
#include <Adafruit_MotorShield.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>

#include "constants.h"
#include "button.h"
#include "temperature_controller.h"
#include "message_handler.h"

class PupaeThermalDevice {

    public:

        PupaeThermalDevice();
        void initialize();
        void update();
        bool enabled();
        void set_enabled(bool enabled);


    protected:

        Adafruit_SH1107 display_ = Adafruit_SH1107(DISPLAY_WIDTH, DISPLAY_HEIGHT, &Wire); 
        Adafruit_MotorShield motor_shield_ = Adafruit_MotorShield();

        TemperatureController temperature_controller_[NUM_CONTROLLER];

        StepButton setpoint_button_[NUM_CONTROLLER] = { 
            StepButton(R_SETP_BUTTON_PIN), 
            StepButton(L_SETP_BUTTON_PIN) 
        };
        Button enable_button_ = Button(ENABLE_BUTTON_PIN);
        MessageHandler msg_handler_;

        std::map<String, std::function<void()>> get_func_table_;
        std::map<String, std::function<void()>> set_func_table_;

        bool enabled_ = false;
        unsigned long t_last_update_= 0;

        void handle_button_input();
        void update_timed_services();
        void update_controllers();
        void update_display();

        void handle_message();
        void on_get_message();
        void on_set_message();

        void on_get_temperature();
        void on_get_ctrl_power();
        void on_get_ctrl_error();
        void on_get_ctrl_ierror();
        void on_get_ctrl_pgain();
        void on_get_ctrl_igain();
        void on_get_ctrl_offset();
        void on_get_ctrl_setpoint();
        void on_get_ctrl_enabled();
        void on_get_all();

        void on_set_ctrl_pgain();
        void on_set_ctrl_igain();
        void on_set_ctrl_setpoint();
        void on_set_ctrl_offset();
        void on_set_ctrl_enabled();

};

#endif
