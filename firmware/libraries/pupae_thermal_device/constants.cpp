#include "constants.h"
#include "SparkFun_STTS22H.h"

const uint32_t LOOP_DT = 40;
const uint32_t SERIAL_BAUDRATE = 115200;

const uint8_t SENSOR_ADDRESS[NUM_CONTROLLER] = {STTS22H_ADDRESS_FIFTEEN, STTS22H_ADDRESS_HIGH};
const char SENSOR_SIDE_LABEL[NUM_CONTROLLER] = {'R', 'L'};

const uint8_t DRIVE_MOTOR_NUMBER[NUM_CONTROLLER] = {3, 4};
const uint32_t DRIVE_MAX_POWER = 4095;

const uint16_t DISPLAY_WIDTH = 64;
const uint16_t DISPLAY_HEIGHT = 128;
const uint8_t DISPLAY_ADDRESS = 0x3D;

const uint8_t R_SETP_BUTTON_PIN = 9;
const uint8_t L_SETP_BUTTON_PIN = 6;
const uint8_t ENABLE_BUTTON_PIN = 5;
const PinMode BUTTON_PIN_MODE = INPUT_PULLUP;
const bool BUTTON_POLARITY = LOW;
const uint32_t BUTTON_DEBOUNCE_PERIOD = 50;
const uint32_t BUTTON_LONG_PRESS_PERIOD = 300;
const uint32_t BUTTON_DOUBLE_CLICK_PERIOD = 300;
const uint32_t BUTTON_DEGLITCH_PERIOD = 10;
const float SETP_STEP_ON_BUTTON_PRESS = 0.1;
extern const unsigned long BUTTON_MIN_STEP_DT_MS = 100;

const float DEFAULT_PGAIN = 100.0;
const float DEFAULT_IGAIN = 0.005;

const float DEFAULT_SETP[NUM_CONTROLLER] = {18.0, 32.0};

const float MIN_SETP_TEMP_C = 16.0;
const float MAX_SETP_TEMP_C = 34.0;

const String MSG_COMMAND = String("command");
const String MSG_ERROR = String("error");
const String MSG_VALUE = String("value");
const String MSG_GET = String("get");
const String MSG_SET = String("set");
const String MSG_TEMPERATURE = String("temperature");
const String MSG_CTRL_ERROR = String("ctrl_error");
const String MSG_CTRL_IERROR = String("ctrl_ierror");
const String MSG_PGAIN = String("pgain");
const String MSG_IGAIN = String("igain");
const String MSG_SETPOINT = String("setpoint");
const String RSP_UNKNOWN_COMMAND = String("unknown command");



