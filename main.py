from display import show_string, show_message
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

    if color == "yellow":
        show_message(display,"String 1")
    if color == "red":
        show_message(display,"String 2")
    if color == "green":
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
