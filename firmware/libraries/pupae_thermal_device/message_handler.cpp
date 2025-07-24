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
        msg_doc_.clear();
        rsp_doc_.clear();
        DeserializationError error = deserializeJson(msg_doc_, receiver_.next());
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
    msg_doc_.clear();
    rsp_doc_.clear();
}

const JsonDocument& MessageHandler::get_message_doc() const {
    return msg_doc_;
}

JsonDocument& MessageHandler::get_response_doc() {
    return rsp_doc_;
}

void MessageHandler::send_response() {
    serializeJson(rsp_doc_, Serial);
    Serial << endl;
}


void MessageHandler::on_json_error(DeserializationError &error) {
    rsp_doc_[MSG_ERROR] = error.c_str();
    send_response();
}


