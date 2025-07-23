#include <Streaming.h>
#include "message_handler.h"

MessageHandler::MessageHandler() {}


void MessageHandler::initialize() {
    receiver_.reset();
}


void MessageHandler::update() {
    have_new_message_ = false;
    receiver_.read_data();
    if (receiver_.available()) {
        msg_json_.clear();
        rsp_json_.clear();
        DeserializationError error = deserializeJson(msg_json_, receiver_.next());
        if (error) {
            on_json_error(error);
        }
        else {
            have_new_message_ = true;
        }
    }
}

bool MessageHandler::new_message() {
    return have_new_message_;
}


void MessageHandler::clear() {
    have_new_message_ = false;
    msg_json_.clear();
    rsp_json_.clear();
}

JsonDocument& MessageHandler::get_message_doc() {
    return msg_json_;
}

JsonDocument& MessageHandler::get_response_doc() {
    return rsp_json_;
}

void MessageHandler::send_response() {
    serializeJson(rsp_json_, Serial);
    Serial << endl;
}


void MessageHandler::on_json_error(DeserializationError &error) {
    rsp_json_[MSG_KEY_ERROR] = error.c_str();
    send_response();
}


