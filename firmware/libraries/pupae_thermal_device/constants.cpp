#include "constants.h"
#include "SparkFun_STTS22H.h"

const uint32_t SERIAL_BAUDRATE = 115200;
const uint32_t LOOP_DT = 40;

const uint8_t SENSOR_ADDRESS[NUM_CONTROLLER] = {STTS22H_ADDRESS_FIFTEEN, STTS22H_ADDRESS_HIGH};
const char SENSOR_SIDE_LABEL[NUM_CONTROLLER] = {'R', 'L'};

const uint8_t DRIVE_MOTOR_NUMBER[NUM_CONTROLLER] = {3, 4};
extern const uint32_t DRIVE_MAX_POWER = 4095;

extern const uint16_t DISPLAY_WIDTH = 64;
extern const uint16_t DISPLAY_HEIGHT = 128;
extern const uint8_t DISPLAY_ADDRESS = 0x3D;
