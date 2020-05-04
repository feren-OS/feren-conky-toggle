#!/usr/bin/python3

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango
from os.path import expanduser

import apt
cache = apt.Cache()

class init():
    stepsdone = ""
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('feren-conky-toggle.glade')
        self.win = self.builder.get_object('MainWind')
        self.win.connect('delete-event', Gtk.main_quit)
        
        self.win.set_icon_name('cs-desklets')

        #Buttons
        self.enableconky = self.builder.get_object('EnableConky')
        self.enableconky.connect('clicked', self.btn_enable)
        self.disableconky = self.builder.get_object('DisableConky')
        self.disableconky.connect('clicked', self.btn_disable)

        #Labels
        

    ### Buttons ###
    def btn_enable(self, button):
        os.system("/usr/bin/conky-toggler on")
        self.enableconky.set_sensitive(False)
        self.disableconky.set_sensitive(True)

    def btn_disable(self, button):
        os.system("/usr/bin/conky-toggler off")
        self.enableconky.set_sensitive(True)
        self.disableconky.set_sensitive(False)

    ### SHOW APP ###
    def run(self):
        global stepsdone
        stepsdone = ""
        if os.path.exists(expanduser("~")+"/.config/autostart/Conky.desktop"):
            self.enableconky.set_sensitive(False)
            self.disableconky.set_sensitive(True)
        else:
            self.enableconky.set_sensitive(True)
            self.disableconky.set_sensitive(False)
        self.win.set_auto_startup_notification(False)
        self.win.show_all()
        self.win.set_auto_startup_notification(True)
        Gtk.main()

if __name__ == '__main__':
    usettings = init()
    usettings.run()
