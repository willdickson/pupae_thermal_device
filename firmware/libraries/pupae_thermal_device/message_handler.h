#ifndef MESSAGE_HANDLER_H
#define MESSAGE_HANDLER_H
#include <ArduinoJson.h>
#include <message_receiver.h>
#include "constants.h"

class MessageHandler {
    
    public:
        MessageHandler();
        void initialize();
        void update();
        bool new_message();
        void send_response();
        void clear();
        const JsonDocument& get_message_doc() const;
        JsonDocument& get_response_doc();
        const JsonObject& get_message_obj() const;

    protected: 
        MessageReceiver<MESSAGE_RECEIVER_SIZE> receiver_;
        JsonDocument msg_doc_;
        JsonDocument rsp_doc_;
        JsonObject msg_obj_;
        bool have_new_message_ = false;
        void on_json_error(DeserializationError &error);

};

#endif
