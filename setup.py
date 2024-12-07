from gpiozero import Button, OutputDevice, LED
from RPLCD.i2c import CharLCD

def setup_lcd(i2cAddress):
    return CharLCD('PCF8574', i2cAddress, cols=16, rows=2)

def setup_buzzer(buzzerPin):
    return OutputDevice(buzzerPin)

def setup_leds(ledConfig):
    leds = {}
    for color, pinNumber in ledConfig.items():
        leds[color] = LED(pinNumber)
    return leds

def setup_buttons(buttonConfig):
    buttons = {}
    for color, pinNumber in buttonConfig.items():
        buttons[color] = Button(pinNumber, hold_time=2)
    return buttons

def setup_hardware():
    ## Hardware info
    i2cAddress = 0x27
    buttonConfig = {
            "green": 27,
            "red": 17,
            "yellow": 22,
            }
    ledConfig = {
            "green": 16,
            "red": 21,
            "yellow": 20,
            }
    buzzerPin = 10
    buzzer = setup_buzzer(buzzerPin)
    buttons = setup_buttons(buttonConfig)
    leds = setup_leds(ledConfig)
    display = setup_lcd(i2cAddress)
    return buzzer, buttons, leds, display
