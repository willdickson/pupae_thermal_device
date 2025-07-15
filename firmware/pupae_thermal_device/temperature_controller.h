#ifndef TEMPERATURE_CONTROLLER_H
#define TEMPERATURE_CONTROLLER_H
#include "constants.h"
#include "Adafruit_MotorShield.h"
#include "SparkFun_STTS22H.h"
#include "peltier_drive.h"



class TemperatureController {

    public:
        TemperatureController();
        void initialize(uint8_t sensor_address, Adafruit_DCMotor *motor);

        void update();
        void update(float ambient);

        float temperature();

        uint8_t sensor_address();

        bool enabled();
        void set_enabled(bool value);

        float setpoint();
        void set_setpoint(float value); 

        float gain();
        void set_gain(float value);

        float ff_slope();
        void set_ff_slope(float value);

        float ambient();
        void set_ambient(float value);

        static constexpr uint32_t SENSOR_SETUP_DT = 100;
        static constexpr float DEFAULT_SETPOINT = 22.0;
        static constexpr float DEFAULT_GAIN = 1.0;
        static constexpr float DEFAULT_FF_SLOPE = 0.0;
        static constexpr float DEFAULT_AMBIENT = 22.0;


    protected:
        SparkFun_STTS22H sensor_;
        PeltierDrive peltier_drive_ = PeltierDrive();

        bool enabled_ = false;
        uint8_t sensor_address_ = 0;
        float setpoint_ = DEFAULT_SETPOINT;
        float gain_ = DEFAULT_GAIN;
        float ff_slope_ = DEFAULT_FF_SLOPE;
        float ambient_ = DEFAULT_AMBIENT;
        float temperature_ = DEFAULT_AMBIENT;

};

#endif
