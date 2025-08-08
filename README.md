## pupae_thermal_device  

A temperature controller for thermal experiments with
Drosophila melanogaster pupea. This device consists of two almuminum plates
separated by a narrow channel in which pupae are placed. Each aluminum plate
has a temperature sensor on the upper surface and sits a Peltier thermoelectric
module.  The temperature of the plates is controlled independently using a
feedback (PID) temperature controller implemented on the an Adafruit Feather
RP2350 in combination with the Adafruit DC Motor Featherwing and Sparkfun's
micro STTS22H temperature sensor. The set-points, plate temperatures and
enabled/disable status are displayed on an Adafruit OLED Featherwing. The three
(A, B, C) buttons on the OLED Fetherwing are used to control the plate set-point temperatures 
and to toggle the controller's enabled/disabled state.

## License: 
Creative Commons Attribution 4.0 International CC BY 4.0



## Device Image 

![screenshot](images/pupae_thermal_device.jpg)


## OLED display and control buttons

![screenshot](images/buttons_figure.png)

The set-point temperatures for the plates and the temperature controller's
state (enabled/disabled) can be controlled using the A, B and C buttons on the
Adafruit OLED Featherwing.

* A/B buttons control right/left plate set-points.  The A/B buttons are
  stateful and will be either in a state where a button press (or hold)
  increases the value or in a state where the button press (or hold) decreases
  the values.  The state can be changed by a quick double press of the button
  where there is less than 0.5s between the two presses.  Slow button presses -
  greater than 0.5s between presses - will increment (or decrement) the
  set-point one step per press.  Pressing and holding the button will cause the
  values to rapidly increment (or decrement). A quick double press of the
  button will change the direction of the steps. 

* The C button can be used to toggle the temperature controllers
  enabled/disabled state. If the text on the OLED screen next to the C button
  says "enabled" then the temperature controllers are enabled. In this case
  pressing the C button this disable the controllers. If the text on the OLED 
  screen next to the C button says "disabled" then pressing the C button will
  disable the temperature controllers.


## Controller tuning GUI 
A simple GUI tool is also available "pupae_thermal_device_tuner" for tuning the
PID controller gains. The tool live streams the systems values - temperature,
setpoint, error, ierror, derror, power - and enables the user to adjust the
set-points and gains of the controllers.  

![screenshot](images/tuner_gui_5.png)



