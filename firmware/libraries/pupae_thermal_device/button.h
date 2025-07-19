#include <avdweb_Switch.h>
#include "constants.h"

class Button : public Switch {

    public:
        Button(uint8_t pin);
        virtual bool poll();
};


class StepButton : public Button {

    public:
        StepButton(uint8_t pin);
        void toggle_sign();
        int32_t sign();
        float step();
        bool step_indicated();
        bool poll();
        bool holding();

    protected:
        int32_t sign_ = 1;
        bool holding_ = false;
        unsigned long t_last_step_ = 0;
};
