#include "pupae_thermal_device.h"
#include <Streaming.h>

PupaeThermalDevice::PupaeThermalDevice() { }

void PupaeThermalDevice::initialize() {
    Wire.begin();
    Serial.begin(SERIAL_BAUDRATE);
    motor_shield_.begin();

    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        Adafruit_DCMotor *motor = motor_shield_.getMotor(DRIVE_MOTOR_NUMBER[i]);
        temperature_controller_[i].initialize(SENSOR_ADDRESS[i], motor);
        temperature_controller_[i].set_enabled(enabled_);
        temperature_controller_[i].set_setpoint(DEFAULT_SETP[i]);
    }

    display_.begin(DISPLAY_ADDRESS, true);
    display_.setRotation(1);
    display_.clearDisplay();
    display_.setTextSize(1);
    display_.setTextColor(SH110X_WHITE);

    // Populate get function table for message handling
    get_func_table_[MSG_TEMPERATURE]   = [this]() {this -> on_get_temperature();};
    get_func_table_[MSG_CTRL_POWER]    = [this]() {this -> on_get_ctrl_power();};
    get_func_table_[MSG_CTRL_ERROR]    = [this]() {this -> on_get_ctrl_error();};
    get_func_table_[MSG_CTRL_IERROR]   = [this]() {this -> on_get_ctrl_ierror();};
    get_func_table_[MSG_CTRL_PGAIN]    = [this]() {this -> on_get_ctrl_pgain();};
    get_func_table_[MSG_CTRL_IGAIN]    = [this]() {this -> on_get_ctrl_igain();};
    get_func_table_[MSG_CTRL_SETPOINT] = [this]() {this -> on_get_ctrl_setpoint();};
    get_func_table_[MSG_CTRL_ENABLED]  = [this]() {this -> on_get_ctrl_enabled();};
    get_func_table_[MSG_ALL]           = [this]() {this -> on_get_all();};

    // Populate set function table for message handling
    set_func_table_[MSG_CTRL_PGAIN]    = [this]() {this -> on_set_ctrl_pgain();};
    set_func_table_[MSG_CTRL_IGAIN]    = [this]() {this -> on_set_ctrl_igain();};
    set_func_table_[MSG_CTRL_SETPOINT] = [this]() {this -> on_set_ctrl_setpoint();};
    set_func_table_[MSG_CTRL_ENABLED]  = [this]() {this -> on_set_ctrl_enabled();};

}

void PupaeThermalDevice::update() {
    handle_message();
    handle_button_input();
    update_timed_services();
}


bool PupaeThermalDevice::enabled() {
    return enabled_;
}


void PupaeThermalDevice::set_enabled(bool enabled) {
    enabled_ = enabled;
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        temperature_controller_[i].set_enabled(enabled_);
    }
}


void PupaeThermalDevice::update_timed_services() {
    unsigned long now = millis();
    unsigned long dt = now - t_last_update_;
    if (dt >= LOOP_DT) {
        update_controllers();
        update_display();
        t_last_update_ = now;
    }
}

void PupaeThermalDevice::update_controllers() { 
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) { 
        temperature_controller_[i].update();
    }
}


void PupaeThermalDevice::handle_button_input() {

    // Check for setpoint update
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        setpoint_button_[i].poll();
        if (setpoint_button_[i].step_indicated()) {
            float step = setpoint_button_[i].step();
            float old_setpoint = temperature_controller_[i].setpoint();
            float new_setpoint = old_setpoint + step; 
            new_setpoint = constrain(new_setpoint, MIN_SETP_TEMP_C, MAX_SETP_TEMP_C);
            temperature_controller_[i].set_setpoint(new_setpoint);
        }
    }

    // Check for change in enable/disable
    enable_button_.poll();
    if (enable_button_.pushed()) {
        enabled_ = !enabled_;
        set_enabled(enabled_);
    }
}


void PupaeThermalDevice::update_display() {
    display_.clearDisplay();
    display_.setCursor(0, 0);
    display_.printf("SIDE  SETP   TEMP (C)");

    uint8_t row_step = 16;
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) { 
        float temp = temperature_controller_[i].temperature();
        float setp = temperature_controller_[i].setpoint();
        display_.setCursor(0, (i+1)*row_step);
        display_.printf("  %c    %3.1f   %3.1f", SENSOR_SIDE_LABEL[i], setp, temp);
    }
    display_.setCursor(0, 3*row_step);
    if (enabled_) {
        display_.printf("  ENABLED");                  
    } 
    else {
        display_.printf("  DISABLED");                  
    }
    display_.display();
}


void PupaeThermalDevice::handle_message() {
    msg_handler_.update();
    if (msg_handler_.new_message()) {
        const JsonDocument &msg_doc = msg_handler_.get_message_doc();
        const char* command_char = msg_doc[MSG_COMMAND];
        if (!command_char) {
            JsonDocument &rsp_doc = msg_handler_.get_response_doc();
            rsp_doc[MSG_ERROR] = String("command is missing or incorrect");
            msg_handler_.send_response();
            return;
        }
        String command = String(command_char);
        if (command == MSG_GET) {
            on_get_message();
        }
        if (command == MSG_SET) {
            on_set_message();
        }
    }
}


void PupaeThermalDevice::on_set_message() {
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    rsp_doc[MSG_COMMAND] = MSG_SET; 
    const JsonObject &msg_obj = msg_handler_.get_message_obj();
    for (auto kv : msg_obj) {
        String key = String(kv.key().c_str());
        if (set_func_table_.count(key)) {
            set_func_table_[key]();
        }
    }
    msg_handler_.send_response();
}


void PupaeThermalDevice::on_get_message() {
    const JsonDocument &msg_doc = msg_handler_.get_message_doc();
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    const char* value_char = msg_doc[MSG_VALUE];
    if (!value_char) {
        rsp_doc[MSG_ERROR] = String("get command missing value key");
    }
    else {
        String value = String(value_char);
        rsp_doc[MSG_COMMAND] = MSG_GET; 
        if (get_func_table_.count(value)) {
            get_func_table_[value]();
        }
        else {
            rsp_doc[MSG_ERROR] = String("set command unknown value");
        }
    }
    msg_handler_.send_response();
}

void PupaeThermalDevice::on_get_temperature() { 
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    JsonArray temp_values = rsp_doc[MSG_TEMPERATURE].to<JsonArray>();
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        temp_values.add(temperature_controller_[i].temperature());
    }
}


void PupaeThermalDevice::on_get_ctrl_power() {
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    JsonArray power_values = rsp_doc[MSG_CTRL_POWER].to<JsonArray>();
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        power_values.add(temperature_controller_[i].power());
    }
}


void PupaeThermalDevice::on_get_ctrl_error() {
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    JsonArray error_values = rsp_doc[MSG_CTRL_ERROR].to<JsonArray>();
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        error_values.add(temperature_controller_[i].error());
    }
}


void PupaeThermalDevice::on_get_ctrl_ierror() {
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    JsonArray ierror_values = rsp_doc[MSG_CTRL_IERROR].to<JsonArray>();
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        ierror_values.add(temperature_controller_[i].ierror());
    }
}


void PupaeThermalDevice::on_get_ctrl_pgain() {
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    JsonArray pgain_values = rsp_doc[MSG_CTRL_PGAIN].to<JsonArray>();
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        pgain_values.add(temperature_controller_[i].pgain());
    }
}


void PupaeThermalDevice::on_get_ctrl_igain() {
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    JsonArray igain_values = rsp_doc[MSG_CTRL_IGAIN].to<JsonArray>();
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        igain_values.add(temperature_controller_[i].igain());
    }
}


void PupaeThermalDevice::on_get_ctrl_setpoint() {
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    JsonArray setpoint_values = rsp_doc[MSG_CTRL_SETPOINT].to<JsonArray>();
    for (uint8_t i=0; i<NUM_CONTROLLER; i++) {
        setpoint_values.add(temperature_controller_[i].setpoint());
    }
}


void PupaeThermalDevice::on_get_ctrl_enabled() {
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    rsp_doc[MSG_CTRL_ENABLED] = enabled_;
}



void PupaeThermalDevice::on_get_all() {
    for (const auto & [key, func] : get_func_table_) {
        if (key == MSG_ALL) {
            continue;
        }
        else {
            func();
        }
    }
}

void PupaeThermalDevice::on_set_ctrl_pgain() {
    const JsonDocument &msg_doc = msg_handler_.get_message_doc();
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
}


void PupaeThermalDevice::on_set_ctrl_igain() {
    const JsonDocument &msg_doc = msg_handler_.get_message_doc();
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
}


void PupaeThermalDevice::on_set_ctrl_setpoint() {
    const JsonDocument &msg_doc = msg_handler_.get_message_doc();
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
}


void PupaeThermalDevice::on_set_ctrl_enabled() {
    const JsonDocument &msg_doc = msg_handler_.get_message_doc();
    JsonDocument &rsp_doc = msg_handler_.get_response_doc();
    if (msg_doc[MSG_CTRL_ENABLED].is<bool>()) {
        set_enabled(msg_doc[MSG_CTRL_ENABLED]);
    }
    else {
        rsp_doc[MSG_ERROR] = String("value, "+ MSG_CTRL_ENABLED + ",  must be bool");
    }
}


