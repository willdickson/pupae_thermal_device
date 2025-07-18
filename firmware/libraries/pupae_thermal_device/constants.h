#ifndef CONSTANTS_H
#define CONSTANTS_H
#include <Arduino.h>

extern const uint32_t SERIAL_BAUDRATE;
extern const uint32_t LOOP_DT;

constexpr uint32_t NUM_CONTROLLER = 2;

extern const uint8_t SENSOR_ADDRESS[NUM_CONTROLLER]; 
extern const char SENSOR_SIDE_LABEL[NUM_CONTROLLER];

extern const uint8_t DRIVE_MOTOR_NUMBER[NUM_CONTROLLER];
extern const uint32_t DRIVE_MAX_POWER;

extern const uint16_t DISPLAY_WIDTH;
extern const uint16_t DISPLAY_HEIGHT;
extern const uint8_t DISPLAY_ADDRESS;


#endif
