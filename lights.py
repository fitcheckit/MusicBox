import time
import board
import neopixel
import math

# Define the number of LEDs and their GPIO pin
NUM_LEDS = 50
LED_PIN = board.D18  # Change this to match your setup

# Initialize the Neopixel library
pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, auto_write=False)

# Function to simulate an easing animation of white pixels
def easing_animation(duration_sec):
    for i in range(NUM_LEDS):
        brightness = int(255 * (1 - math.pow(1 - i / NUM_LEDS, 2)))  # Easing out
        pixels[i] = (brightness, brightness, brightness)
        pixels.show()
        time.sleep(duration_sec / NUM_LEDS)

# Simulate the easing animation for 5 seconds
easing_animation(3)

# Turn off all LEDs
pixels.fill((0, 0, 0))
pixels.show()