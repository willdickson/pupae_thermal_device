#include <Streaming.h>
#include <ArduinoJson.h>
#include "message_receiver.h"

constexpr size_t BUFFER_SIZE = 2000;

MessageReceiver<BUFFER_SIZE> mr;

void setup() {
    Serial.begin(115200);
    mr.reset();
}

void loop() {
    mr.read_data();
    if (mr.available()) {
        JsonDocument doc;
        DeserializationError error = deserializeJson(doc, mr.next());
        if (error) {
            Serial << "error: " << error.c_str() << endl;
        }
        else {
            Serial << "message: "; 
            serializeJson(doc, Serial);
            Serial << endl;
        }
    }
}
