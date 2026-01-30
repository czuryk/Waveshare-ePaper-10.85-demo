#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
import time
import logging
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# пути
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
libdir = os.path.join(BASE_DIR, 'lib')
fntdir = os.path.join(BASE_DIR, 'fnt')

if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd10in85

logging.basicConfig(level=logging.INFO)

try:
    epd = epd10in85.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(0.5)

    logging.info("EPD size: %dx%d", epd.width, epd.height)

    logging.info("Drawing")
    #font_path = os.path.join(fntdir, "Font.ttc")
    font24 = ImageFont.truetype(os.path.join(fntdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(fntdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(fntdir, 'Font.ttc'), 35)
    font300 = ImageFont.truetype(os.path.join(fntdir, 'advanced_led_board-7.ttc'), 300)

    # partial update
    logging.info("show time")
    epd.init_Part()
    # # If you did not use epd.display_Base_color or epd.display_Base to refresh previously,
    # # you will need to use these two functions for a refresh, or the local brush display will be problematic
    Himage = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(Himage)
    num = 0
    while (True):
        #draw.rectangle((681, 0, 1359, 479), fill=0)
        draw.rectangle((0, 0, epd.width, epd.height), fill=255)

        draw.text((120, 120), time.strftime('%H:%M:%S'), font=font300, fill=0)
        #newimage = Himage.crop([10, 110, 120, 150])
        #Himage.paste(newimage, (10,110))
        epd.display_Partial(epd.getbuffer(Himage), 0, 0, epd.width, epd.height)
        num = num + 1
        print(num)
        #time.sleep(10)
        if (num == 10):
            break

    logging.info("Clear...")
    epd.init()
    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd10in85.epdconfig.module_exit(cleanup=True)
    exit()
