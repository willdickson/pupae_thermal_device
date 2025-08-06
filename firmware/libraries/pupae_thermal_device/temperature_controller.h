#ifndef TEMPERATURE_CONTROLLER_H
#define TEMPERATURE_CONTROLLER_H
#include "constants.h"
#include "Adafruit_MotorShield.h"
#include "SparkFun_STTS22H.h"
#include "peltier_drive.h"
#include "lowpass_filter.h"



class TemperatureController {

    public:
        TemperatureController();
        void initialize(uint8_t sensor_address, Adafruit_DCMotor *motor);

        void update();

        float temperature();
        float power();
        float error();
        float ierror();
        float derror();

        uint8_t sensor_address();

        bool enabled();
        void set_enabled(bool value);

        float setpoint();
        void set_setpoint(float value); 

        float pgain();
        void set_pgain(float value);

        float igain();
        void set_igain(float value);

        float dgain();
        void set_dgain(float value);

        float offset();
        void set_offset(float value);

        static constexpr uint32_t SENSOR_SETUP_DT = 100;
        static constexpr float DEFAULT_SETPOINT = 22.0;


    protected:
        SparkFun_STTS22H sensor_;
        uint8_t sensor_address_ = 0;

        PeltierDrive peltier_drive_ = PeltierDrive();

        bool enabled_ = false;
        bool is_first_ = false;
        unsigned long t_last_us_ = 0;

        float temperature_ = 0.0;
        float setpoint_ = DEFAULT_SETPOINT;

        float pgain_ = DEFAULT_PGAIN;
        float igain_ = DEFAULT_IGAIN;
        float dgain_ = DEFAULT_DGAIN;
        float offset_ = 0.0;

        float power_ = 0.0;
        float error_ = 0.0;
        float ierror_ = 0.0;
        float derror_ = 0.0;
        float error_last_ = 0.0;
        LowpassFilter derror_lowpass_ = LowpassFilter(DGAIN_LOWPASS_CUTOFF_FREQ, 0.0);

};

#endif
