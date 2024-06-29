import os
import subprocess as sp

class OfflineOperations:
    paths = {
        'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
        'discord': "C:\\Users\\carlo\\AppData\\Local\\Discord\\app-1.0.9151\\Discord.exe",
        'calculator': "C:\\Windows\\System32\\calc.exe"
    }
    def __init__(self):
        pass
    
    def open_camera(self):
        """Opens windows camera"""
        sp.run('start microsoft.windows.camera:', shell=True)

    def open_notepad(self):
        """Opens notepad++"""
        os.startfile(paths['notepad'])

    def open_discord(self):
        """Opens discord"""
        os.startfile(paths['discord'])

    def open_cmd(self):
        """Opens command prompt"""
        os.system('start cmd')

    def open_calculator(self):
        """Opens calculator app"""
        sp.Popen(paths['calculator'])

if __name__ == "__main__":
    test_ = OfflineOperations()