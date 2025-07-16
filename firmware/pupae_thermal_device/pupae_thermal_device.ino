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
}



