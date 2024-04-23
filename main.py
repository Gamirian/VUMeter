import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

#setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,  # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

def update_leds(volume, num_leds):
    light_intensity = (volume-20000)/1750
    print(light_intensity)
    for i, led in enumerate(leds):
        led.value = i<light_intensity

while True:
    volume = microphone.value
    print(volume)
    update_leds(volume, len(leds))
    sleep(0.1)