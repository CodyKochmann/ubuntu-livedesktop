# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-09 10:32:44
# @Last Modified 2016-12-09
# @Last Modified time: 2016-12-09 11:52:05

from PIL import Image, ImageDraw, ImageFont
from veripy import veripy

target_file = "background.jpg"
output_file = "tmp.background.jpg"

settings={
    'font-file':"liberation-mono-regular.ttf",
    'color':(255,255,255,255),

}

def change_wallpaper(path):
    veripy.str(path)
    veripy.not_empty(path)
    from os import system as bash
    from os.path import abspath
    from os.path import isfile
    path = abspath(path)
    assert isfile(path)
    bash('gsettings set org.gnome.desktop.background picture-uri "file://{}"'.format(path))

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

#=====================================================================

base = Image.open(target_file)

from display_items import display_items

for m in display_items:
    base = add_text(
        base,
        *m
    )

base.save(output_file)
change_wallpaper(output_file)
