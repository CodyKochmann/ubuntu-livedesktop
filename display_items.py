# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-09 11:44:47
# @Last Modified 2016-12-10
# @Last Modified time: 2016-12-10 12:41:43

settings={
    # path to the desktop background
    'background-path':'background.jpg',
    # path to the font file used
    'font-file':"liberation-mono-regular.ttf",
    # color of font to be put on the background
    'color':(255,255,255,255)
}

#==========================================================

def clock_display(): # returns time in minutes and hours
    from time import localtime, strftime
    #strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return strftime("%H:%M", localtime())

#==========================================================

display_items=[
    # ("Hello World!",50,10,60),
    (clock_display(),85,83,180)
]

if __name__ == "__main__":
    for i in display_items:
        print i
