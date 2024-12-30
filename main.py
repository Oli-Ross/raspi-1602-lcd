from display import show_message
from setup import setup_hardware

from random import randint
from signal import pause
from functools import partial

def set_callbacks(buttons):
    for color, button in buttons.items():
        button.when_held = partial(callback_held,color)
        button.when_pressed = partial(callback_press,color)
        button.when_released = partial(callback_release, color) 

def callback_held(color):
    global display
    display.clear()

def callback_release(color):
    global leds
    leds[color].off()

def callback_press(color):
    global display
    global buzzer
    buttons[color].when_pressed = None
    leds[color].on()

    if color == "green":
        greentext = "This is a rather long story about someone using a Raspberry Pi, to learn how to program an I2C 16x02 LCD Display and controlling it with buttons."
        show_message(display,greentext)
    if color == "yellow":
        show_message(display,"String 2")
    if color == "red":
        show_message(display,"String 3")
    buttons[color].when_pressed = partial(callback_press,color)
    # buzzer.on()
    # show_string(display, str(globalCount))

buzzer, buttons, leds, display = setup_hardware()
set_callbacks(buttons)

try:
    pause()
except KeyboardInterrupt:
    display.clear()
