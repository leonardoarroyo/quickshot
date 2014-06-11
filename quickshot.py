#!/usr/bin/env python

import subprocess
import sys
import re
import os.path
import json

# Check for wxPython
try:
    import wx
except:
    sys.exit('You need wxPython.')

# Check for xrectsel
if not (subprocess.Popen("command -v xrectsel", stdout=subprocess.PIPE, shell=True).communicate()[0]):
    sys.exit('You need xrectsel. Make sure it\'s on your PATH.')

class QuickShot:
    path = './'
    prefix = 'screenshot'

    def __init__(self, settings={}):
        for k, v in settings.iteritems():
            if k == 'path':
                self.path = v
            if k == 'prefix':
                self.prefix = v

    def grab_position(self):
        """ Uses xrectsel utility to grab screenshot position """

        xrectsel_output = subprocess.Popen("xrectsel", stdout=subprocess.PIPE, shell=True).communicate()[0]
        regex = re.compile(r"^(?P<width>\d+)x(?P<height>\d+)\+(?P<x>\d+)\+(?P<y>\d+)$")
        pos = regex.match(xrectsel_output).groupdict()
        for k in pos: pos[k] = int(pos[k])
        self.pos = pos

    def take_screenshot(self, properties=None):
        """ Takes screenshot. If properties not set, it will use QuickShot.grab_position
            to get the necessary parameters.
            properties = dictionary {'width':int, 'height':int, 'x':int, 'y':int}"""

        if not properties:
            properties = self.grab_position()

        # Preparing wx app
        app = wx.App()
        screen = wx.ScreenDC()

        # Creating bitmap
        self.bmp = wx.EmptyBitmap(self.pos['width'], self.pos['height'])
        mem = wx.MemoryDC(self.bmp)
        mem.Blit(0, 0, self.pos['width'], self.pos['height'], screen, self.pos['x'], self.pos['y'])
        del mem  # Release bitmap

    def save_screenshot(self, prefix=None, name=None):
        """ Save screenshot to specified path """
        if not prefix:
            prefix = self.prefix
        if not name:
            name = ''
        self.bmp.SaveFile('{}{}{}.png'.format(os.path.expanduser(self.path), prefix, name), wx.BITMAP_TYPE_PNG)

if __name__ == '__main__':
    with open('config') as fin:
        settings = json.load(fin)
    
    qs = QuickShot(settings)
    qs.take_screenshot()
    qs.save_screenshot(name=str(settings['count']))

    settings['count'] += 1
    with open('config', 'w') as out:
        json.dump(settings, out)