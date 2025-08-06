#ifndef LOWPASS_FILTER_H
#define LOWPASS_FILTER_H

class LowpassFilter {

    public:
        LowpassFilter(float cut_freq=1.0, float ini_val=0.0);

        float update(float new_val, float dt);

        void reset();
        void reset(float ini_val);

        float get_cut_freq();
        void set_cut_freq(float cut_freq);

        float get_ini_val();
        void set_ini_val(float ini_val);

        float get_val();


    protected:
        float cut_freq_ = 1.0;
        float ini_val_ = 0.0;
        float val_ = 0.0;
};

#endif
