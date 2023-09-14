from subprocess import Popen
import os
import wmi
computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
desktop_path= rf"C:\Users\{computer_info.PrimaryOwnerName}\Desktop\\"

def spotify():
    Popen(desktop_path+"Spotify.lnk",shell=True)
def valorant():
    Popen(desktop_path+"Valorant.lnk",shell=True)
def linkedin():
    Popen(desktop_path+"LinkedIn.lnk",shell=True)
def steam():
    Popen(desktop_path+"Steam.lnk",shell=True)
def tureng():
    Popen(desktop_path+"Tureng.lnk",shell=True)
def Netflix():
    Popen(desktop_path+"Netflix.lnk",shell=True)
def Github():
    Popen(desktop_path+"Github Desktop.lnk",shell=True)
def Google():
    Popen("start chrome ",shell=True)

