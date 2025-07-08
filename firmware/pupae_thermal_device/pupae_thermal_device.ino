#include <Wire.h>
#include <Streaming.h>
#include "SparkFun_STTS22H.h"

SparkFun_STTS22H temp_sensor;

void setup() {
    Wire.begin();
    Serial.begin(115200);

    Serial << "setting up temp_sensor" << endl;
    //if (!temp_sensor.begin(Wire1, STTS22H_ADDRESS_FIFTEEN)) {
    while (!temp_sensor.begin(STTS22H_ADDRESS_FIFTEEN)) {
        Serial << "  temp_sensor failed to begin" << endl;
        delay(100);
    }

    temp_sensor.setDataRate(STTS22H_POWER_DOWN);
    delay(10);
    temp_sensor.setDataRate(STTS22H_25Hz);
    temp_sensor.enableAutoIncrement();
    delay(100);
    Serial << "temp_sensor ready" << endl;
}

void loop() {
    static uint32_t count = 0;
    if (temp_sensor.dataReady()) {
        float temp;
        temp_sensor.getTemperatureC(&temp);

        Serial << "count = " << count << ", " << "temp = " << temp << endl;
        count += 1;
    }
    delay(40);
}


