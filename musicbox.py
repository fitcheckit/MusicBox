#!/usr/bin/venv python3
# MUSICBOX 0.1 
import os
from escpos.printer import Usb
from escpos.escpos import Escpos
from PIL import Image
import RPi.GPIO as GPIO
from datetime import date
import time
import sys

imagecounter = 1
global duplicate_image_dealer 
duplicate_image_dealer = 1

# p = Usb(0x0fe6, 0x811e)

def button_callback(channel):
    newcounter = 1
    time.sleep(1)
    # activate light here, keep on

    p.set(
        align="center",
        font="b",
        # bold=True,
        # underline=0,
        width=1,
        height=1,
    )

    # p.text("*--------Musicbox-------*")
    p.image("logosmall.png")
    # today = date.today()
    # d2 = today.strftime("\n%B %d, %Y")
    # p.text(str(d2))
    p.text("9/19/23")
    p.text("\n \nFeaturing three young artists, this playlist\n captures what todays indie youth has to say.")


    # p.text("\n#" + str(newcounter) + "/100   ")
    p.text("\n\nMidnight Freak-Out - Sofia Valdes")
    p.text("\nFor You - Superfan")
    p.text("\nAUTO - Stevan\n")



    p.set(
        align="center",
        font="b",
        # bold=True,
        # underline=0,
        width=1,
        height=1,
    )

    p.text("\nSpotify")

    p.qr(
            "https://open.spotify.com/playlist/4cw7znfB6bROAAgVaeykze?si=5b06b0c90c2f403b",
            ec=0,
            size=3,
            model=2,
            native=False,
            # center=False,
            impl="bitImageRaster",
        )

    p.set(
        align="center",
        font="b",
        # bold=True,
        # underline=0,
        width=1,
        height=1,
    )

    p.text("Apple Music")


    p.qr(
            "https://music.apple.com/us/playlist/indie-tuesday/pl.u-jV890gWtDpW7mYJ",
            ec=0,
            size=3,
            model=2,
            native=False,
            # center=False,
            impl="bitImageRaster",
        )

    p.text("follow @musicbox.playlists")


    p.cut(mode="PART")

    newcounter = newcounter + 1
    print ("great job man, lets do it again")
    counter = 1
    if counter == 1:
        GPIO.output (8, GPIO.HIGH)

def button_event_handler(pin):
    global duplicate_image_dealer
    print("event detection occured")
    button_callback(10)

        
        
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
# message = input("hello")

counter = 1
if counter == 1:
    GPIO.output (8, GPIO.HIGH)



GPIO.add_event_detect(10,GPIO.FALLING,callback=button_event_handler)

while 1==1:
            x = 1



GPIO.cleanup()
