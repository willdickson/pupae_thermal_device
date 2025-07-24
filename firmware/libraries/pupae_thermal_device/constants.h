#ifndef CONSTANTS_H
#define CONSTANTS_H
#include <Arduino.h>

constexpr uint32_t NUM_CONTROLLER = 2;
constexpr size_t MESSAGE_RECEIVER_SIZE = 2000;

extern const uint32_t LOOP_DT;
extern const uint32_t SERIAL_BAUDRATE;

extern const uint8_t SENSOR_ADDRESS[NUM_CONTROLLER]; 
extern const char SENSOR_SIDE_LABEL[NUM_CONTROLLER];

extern const uint8_t DRIVE_MOTOR_NUMBER[NUM_CONTROLLER];
extern const uint32_t DRIVE_MAX_POWER;

extern const uint16_t DISPLAY_WIDTH;
extern const uint16_t DISPLAY_HEIGHT;
extern const uint8_t DISPLAY_ADDRESS;

extern const uint8_t R_SETP_BUTTON_PIN;
extern const uint8_t L_SETP_BUTTON_PIN;
extern const uint8_t ENABLE_BUTTON_PIN;
extern const PinMode BUTTON_PIN_MODE;
extern const bool BUTTON_POLARITY;
extern const uint32_t BUTTON_DEBOUNCE_PERIOD;
extern const uint32_t BUTTON_LONG_PRESS_PERIOD;
extern const uint32_t BUTTON_DOUBLE_CLICK_PERIOD;
extern const uint32_t BUTTON_DEGLITCH_PERIOD;
extern const float SETP_STEP_ON_BUTTON_PRESS;
extern const unsigned long BUTTON_MIN_STEP_DT_MS;

extern const float DEFAULT_PGAIN;
extern const float DEFAULT_IGAIN;
extern const float DEFAULT_SETP[NUM_CONTROLLER];

extern const float MIN_SETP_TEMP_C;
extern const float MAX_SETP_TEMP_C;

extern const String MSG_COMMAND;
extern const String MSG_ERROR; 
extern const String MSG_VALUE;
extern const String MSG_GET; 
extern const String MSG_SET; 
extern const String MSG_TEMPERATURE;
extern const String MSG_CTRL_POWER;
extern const String MSG_CTRL_ERROR;
extern const String MSG_CTRL_IERROR;
extern const String MSG_CTRL_PGAIN;
extern const String MSG_CTRL_IGAIN;
extern const String MSG_CTRL_SETPOINT;
extern const String MSG_CTRL_ENABLED;
extern const String MSG_ALL;
extern const String RSP_UNKNOWN_COMMAND;

#endif
