#include "button.h"

// Button
// ----------------------------------------------------------------------------
Button::Button(uint8_t pin)  
    : Switch(
            pin, 
            BUTTON_PIN_MODE, 
            BUTTON_POLARITY, 
            BUTTON_DEBOUNCE_PERIOD, 
            BUTTON_LONG_PRESS_PERIOD, 
            BUTTON_DOUBLE_CLICK_PERIOD, 
            BUTTON_DEGLITCH_PERIOD
            )
{ }

bool Button::poll() {
    bool switched = Switch::poll();
    return switched;
}




// StepButton
// ----------------------------------------------------------------------------

StepButton::StepButton(uint8_t pin)
    : Button(pin) 
{}

float StepButton::step() {
    return sign_*SETP_STEP_ON_BUTTON_PRESS;
}

bool StepButton::poll() { 
    bool switched = Button::poll();
    if (longPress()) {
        holding_ = true;
    }
    if (released()) {
        holding_ = false;
    }
    if (doubleClick()) {
        toggle_sign();
    }
    return switched;
}

bool StepButton::holding() {
    return holding_;
}

void StepButton::toggle_sign() {
    sign_ *= -1;
}

int32_t StepButton::sign() {
    return sign_;
}

bool StepButton::step_indicated() {
    bool rval= false;
    if (pushed() || holding()) {
        unsigned long now = millis();
        unsigned long dt = now - t_last_step_;
        if (dt >= BUTTON_MIN_STEP_DT_MS ) {
            rval = true;
            t_last_step_ = now;
        }
    }
    return rval;
}
