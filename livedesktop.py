# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-09 10:32:44
# @Last Modified 2016-12-11
# @Last Modified time: 2016-12-11 08:09:30

from PIL import Image, ImageDraw, ImageFont
from veripy import veripy

from display_items import display_items, settings

#output_file = "tmp.background.jpg"

def timestamp(human_readable=False):
    # Generates a unix timestamp and a human readable timestamp if passed True
    # by: Cody Kochmann
    from calendar import timegm
    from datetime import datetime
    if human_readable:
        return(datetime.now())
    else:
        return(timegm(datetime.now().utctimetuple()))


def change_wallpaper(path):
    veripy.str(path)
    veripy.not_empty(path)
    from os import system as bash
    from os.path import abspath
    from os.path import isfile
    path = abspath(path)
    assert isfile(path)
    bash('chbackground "{}"'.format(path))

def add_text(base,message,top,left,fontsize):
    veripy.str(message)
    veripy.int(fontsize,top,left)

    # locations are in percentages so
    assert top<101 and top>-1
    assert left<101 and left>-1
    # convert the percentages into positions on base
    location = (
        base.size[0]*(left/100.0),
        base.size[1]*(top/100.0)
    )

    base = base.convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    text_layer = Image.new(
        'RGBA',
        base.size,
        (255,255,255,0)
    )
    # get a drawing context
    draw = ImageDraw.Draw(text_layer)
    # add the text
    draw.text(
        location,
        message,
        font=ImageFont.truetype(settings['font-file'], fontsize),
        fill=settings['color']
    )
    # combine the two layers
    return Image.alpha_composite(base, text_layer)

def clean_tmp_images():
    from os import system
    system("rm tmp.*.jpg")

#=====================================================================

def main():
    global settings
    output_file = "tmp.{}.jpg".format(timestamp())
    base = Image.open(settings['background-path'])

    for m in display_items:
        base = add_text(
            base,
            *m
        )
    clean_tmp_images()
    base.save(output_file)
    change_wallpaper(output_file)

def restart_script():
    from os import system
    system("nohup python livedesktop.py >> /dev/null &")
    exit()

if __name__ == '__main__':
    from time import sleep
    main()
    sleep(10)
    restart_script()
