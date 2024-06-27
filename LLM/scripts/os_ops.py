import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\carlo\\AppData\\Local\\Discord\\app-1.0.9151\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_camera():
    """Opens windows camera"""
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    """Opens notepad++"""
    os.startfile(paths['notepad'])

def open_discord():
    """Opens discord"""
    os.startfile(paths['discord'])

def open_cmd():
    """Opens command prompt"""
    os.system('start cmd')

def open_calculator():
    """Opens calculator app"""
    sp.Popen(paths['calculator'])

