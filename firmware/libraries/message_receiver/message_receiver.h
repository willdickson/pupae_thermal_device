#ifndef MESSAGE_RECEIVER_H 
#define MESSAGE_RECEIVER_H

#include <Arduino.h>
#include <CircularBuffer.hpp>

template <size_t MAX_SIZE>
class MessageReceiver
{

    public:

        MessageReceiver();
        void reset();
        void read_data();
        String next();
        bool available() const;
        uint32_t get_message_count() const;
        uint32_t get_total_message_count() const;

    protected:

        CircularBuffer<char,MAX_SIZE> serial_buffer_;
        bool overflow_ = false;
        uint32_t message_count_ = 0;
        uint32_t total_message_count_ = 0;
};


template <size_t MAX_SIZE>
MessageReceiver<MAX_SIZE>::MessageReceiver() { }


template <size_t MAX_SIZE>
void MessageReceiver<MAX_SIZE>::reset()
{
    overflow_ = false;
    message_count_ = 0;
}


template <size_t MAX_SIZE>
void MessageReceiver<MAX_SIZE>::read_data()
{
    while(Serial.available() > 0)
    {
        char byte = Serial.read();
        if (!serial_buffer_.isFull())
        {
            serial_buffer_.push(byte);
            if (byte == '\n')
            {
                message_count_++;
                total_message_count_++;
            }
        }
        else
        {
            overflow_ = true;
        }
    }
}


template <size_t MAX_SIZE>
String MessageReceiver<MAX_SIZE>::next()
{
    String message("");
    if (message_count_ > 0)
    {
        {  // Begin atomic block  
            while (!serial_buffer_.isEmpty())
            {
                char byte = serial_buffer_.shift();
                if (byte == '\n')
                {
                    break;
                }
                message += String(byte);
            }
            message_count_--;
        } // End atomic block
    }
    return message;
}


template <size_t MAX_SIZE>
bool MessageReceiver<MAX_SIZE>::available() const
{
    return (message_count_ > 0);
}


template <size_t MAX_SIZE>
uint32_t MessageReceiver<MAX_SIZE>::get_message_count() const
{
    return message_count_;
}


template <size_t MAX_SIZE>
uint32_t MessageReceiver<MAX_SIZE>::get_total_message_count() const
{
    return total_message_count_;
}




#endif
