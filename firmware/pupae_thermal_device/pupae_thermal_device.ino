#include <Wire.h>
#include <Streaming.h>
//#include "SparkFun_STTS22H.h"
//#include "Adafruit_MotorShield.h"
#include "pupae_thermal_device.h"

PupaeThermalDevice device = PupaeThermalDevice();

void setup() {
    device.initialize();
}

void loop() {

    device.update();

    //static uint32_t count = 0;

    //Serial << "count = " << count << endl;

    //count++;
    //delay(500);
}



//constexpr uint32_t NUM_DEV = 2;
//const uint8_t SENSOR_ADDRESS[NUM_DEV] = {STTS22H_ADDRESS_FIFTEEN, STTS22H_ADDRESS_HIGH};
//SparkFun_STTS22H temp_sensor[NUM_DEV];
//Adafruit_MotorShield motor_shield = Adafruit_MotorShield();
//
//
//void setup() {
//    Wire.begin();
//    Serial.begin(115200);
//    motor_shield.begin();
//
//    for (uint8_t i=0; i<NUM_DEV; i++) {
//        Serial << "setting up temp_sensor" << endl;
//        while (!temp_sensor[i].begin(SENSOR_ADDRESS[i])) {
//            Serial << "  temp_sensor failed to begin" << endl;
//            delay(100);
//        }
//
//        temp_sensor[i].setDataRate(STTS22H_POWER_DOWN);
//        delay(10);
//        temp_sensor[i].setDataRate(STTS22H_25Hz);
//        temp_sensor[i].enableAutoIncrement();
//        delay(100);
//        Serial << "temp_sensor ready" << endl;
//    }
//
//    //for (uint8_t i=1; i<=2; i++) {
//    //    Adafruit_DCMotor *motor = motor_shield.getMotor(i);
//    //    motor -> setSpeed(255);
//    //    motor -> run(FORWARD);
//    //}
//
//}
//
//void loop() {
//
//    uint8_t speed3 = 0;
//    uint8_t speed4 = 0;
//
//    Adafruit_DCMotor *motor3 = motor_shield.getMotor(3);
//    motor3 -> setSpeed(speed3);
//    motor3 -> run(FORWARD);
//    //motor4 -> run(BACKWARD);
//
//    Adafruit_DCMotor *motor4 = motor_shield.getMotor(4);
//    motor4 -> setSpeed(speed4);
//    //motor4 -> run(FORWARD);
//    motor4 -> run(BACKWARD);
//
//
//    for (uint8_t i=0; i<NUM_DEV; i++) {
//        if (temp_sensor[i].dataReady()) {
//            float temp;
//            temp_sensor[i].getTemperatureC(&temp);
//            Serial << "temp = " << temp << " (C)" << endl;
//        }
//    }
//    Serial << endl;
//    //delay(1000);
//    delay(50);
//}


