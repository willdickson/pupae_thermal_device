#include "lowpass_filter.h"
#include <cmath>

LowpassFilter::LowpassFilter(float cut_freq, float ini_val) {
    set_ini_val(ini_val);
    set_cut_freq(cut_freq);
    reset();
}

float LowpassFilter::update(float new_val, float dt) {
    float rc = 1.0/(2.0*M_PI*cut_freq_);
    float alpha =  dt/(rc + dt);
    val_ = alpha*new_val + (1-alpha)*val_;
    return val_;
}

void  LowpassFilter::reset() {
    val_ = ini_val_;
}

void  LowpassFilter::reset(float ini_val) {
    set_ini_val(ini_val);
    reset();
}

 float LowpassFilter::get_cut_freq() {
     return cut_freq_;
 }

 void LowpassFilter::set_cut_freq(float cut_freq) {
     cut_freq_ = fabs(cut_freq);
 }

 float LowpassFilter::get_ini_val() {
     return ini_val_;
 }

 void LowpassFilter::set_ini_val(float ini_val){
     ini_val_ = ini_val;
 }

float LowpassFilter::get_val() {
    return val_;
}
