#include "constants.h"
#include "SparkFun_STTS22H.h"

const uint32_t SERIAL_BAUDRATE = 115200;
const uint32_t LOOP_DT = 40;

const uint8_t SENSOR_ADDRESS[NUM_CONTROLLER] = {STTS22H_ADDRESS_FIFTEEN, STTS22H_ADDRESS_HIGH};
const uint8_t DRIVE_MOTOR_NUMBER[NUM_CONTROLLER] = {3, 4};
