#include <Streaming.h>
#include "message_receiver.h"

constexpr size_t BUFFER_SIZE = 2000;

MessageReceiver<BUFFER_SIZE> mr;

void setup() {
    Serial.begin(115200);
    mr.reset();
}


void loop() {
    static uint32_t cnt = 0;
    mr.read_data();

    if (mr.available()) {
        String message = mr.next();
        Serial << "message = " << message <<  endl;
    }
}

