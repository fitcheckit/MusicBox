# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import adafruit_fancyled.adafruit_fancyled as fancy
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
BRIGHTNESS = 1.0

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER
)


def gradual_brightness_increase(duration):
        target_brightness = 1.0
        num_steps = 100
        brightness_step = target_brightness / num_steps

        for step in range (num_steps + 1):
            current_brightness = step * brightness_step 
            pixels.brightness = current_brightness

            pixels.fill((255,255,255))
            pixels.show()

            time.sleep(duration / num_steps)


def flashes ():

    x = 0
    pixels.brightness = 0

    while x < 3:
        pixels.fill((255,255,150))
        pixels.brightness = 0.1
        pixels.show ()
        time.sleep(.5)
        pixels.fill((0,0,0))      
        pixels.show ()
        time.sleep(.5)
        x = x + 1
        pixels.brightness = pixels.brightness + 0.5

def turn_one_by_one(duration):
    # for i in range(num_pixels):
        gradual_brightness_increase(1)
        pixels.fill(255,255,255)
        pixels.show()

# rgb = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)


import time



def moving_gradients():
    BRIGHTNESS = .2
    WHITE = fancy.CRGB(255, 255, 255)
    BLACK = fancy.CRGB(0, 0, 0)
    RED = fancy.CRGB(255, 255, 255)
    GREEN = fancy.CRGB(230, 23, 255)
    YELLOW = fancy.CRGB(255, 255, 0)
    BLUE = fancy.CRGB(0, 0, 255)
    ORANGE = fancy.CRGB(10, 127, 0)
    VIOLET = fancy.CRGB(139, 0, 255)

    gradient = fancy.expand_gradient([
        (0.0, RED),
        # (0.16, ORANGE),
        # (0.33, YELLOW),
        (0.5, GREEN),
        # (0.66, BLUE),
        # (0.82, VIOLET),
        (1.0, RED)
    ], 1000)

    index = 0

    while True:
        color = gradient[index]
        adjusted = fancy.gamma_adjust(color, brightness=BRIGHTNESS)
        pixels.fill(adjusted.pack())
        pixels.write()

        index += 1
        if index > len(gradient)-1:
            index = 0

        time.sleep(0.01)


pixels.fill((0,0,0))
pixels.show ()

flashes()
gradual_brightness_increase(2)


pixels.fill((0,0,0))
pixels.show ()
time.sleep(1)
moving_gradients()