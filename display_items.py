# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-09 11:44:47
# @Last Modified 2016-12-09
# @Last Modified time: 2016-12-09 11:58:18

def clock_display(): # returns time in minutes and hours
    from time import localtime, strftime
    #strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return strftime("%H:%M", localtime())

#=====================================================================

display_items=[
    # ("Hello World!",50,10,60),
    (clock_display(),85,83,180)
]

if __name__ == "__main__":
    for i in display_items:
        print i
