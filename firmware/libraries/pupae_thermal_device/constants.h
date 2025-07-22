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

#endif
