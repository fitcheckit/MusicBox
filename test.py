#!/usr/bin/venv python3
# MUSICBOX 0.1 
import os
from PIL import Image
import RPi.GPIO as GPIO
from datetime import date
import time
import sys
# import escpos
from escpos.printer import Usb
from escpos.escpos import Escpos

imagecounter = 1
global duplicate_image_dealer 
duplicate_image_dealer = 1

newcounter = 1

# activate light here, keep on

p = Usb(0x0fe6, 0x811e)

p.set(
align="center",
font="a",
# bold=True,
# underline=0,
width=1,
height=1,
)

p.text("Musicbox\n\n\n")

# p.text("\n#" + str(newcounter) + "/100   ")
p.text("\nmakeoutsong - alesloveletters")
p.text("\The Race - Tay-K")
p.text("\Something About You - Hayden James")

today = date.today()
d2 = today.strftime("\n%B %d, %Y")
p.text(str(d2))
# p.text("\nCheckpoint")



p.set(
align="left",
font="b",
# bold=True,
# underline=0,
width=1,
height=1,
)

# p.qr(
#         "https://open.spotify.com/playlist/4ybdcQONNCPS72uCfcQRg3?si=K9CwLUiGSimPe472xqKUVghttps://open.spotify.com/playlist/4ybdcQONNCPS72uCfcQRg3?si=K9CwLUiGSimPe472xqKUVg",
#         ec=0,
#         size=3,
#         model=2,
#         native=False,
#         # center=False,
#         impl="bitImageRaster",
#     )

p.set(
align="center",
font="a",
# bold=True,
# underline=0,
width=1,
height=1,
)

p.cut(mode="PART")