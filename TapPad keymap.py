import tappad
import keyboard
import screen_brightness_control as sbc
import os
import wizapi
import time
import webbrowser
import subprocess
from pathlib import Path

we = Path("add path")

wallpapers = {
    "red":r"add path",
    "green":r"add path",
    "blue":r"add path",
    "white":r"add path"
}

led_state = tappad.set_rgb(255,255,255,100)
x = 0

while 1:
    event = keyboard.read_event()
    if event.name == "f13":
        tappad.set_rgb(255,0,0,100)
        wizapi.send_config({"state": True,"dimming":70,"r":255})
        subprocess.run([
            str(we),
            "-control", "openWallpaper",
            "-file", str(Path(wallpapers["red"]))
        ], check=True)
    if event.name == "f14":
        tappad.set_rgb(0,255,0,100)
        wizapi.send_config({"state": True,"dimming":70,"g":255})
        subprocess.run([
            str(we),
            "-control", "openWallpaper",
            "-file", str(Path(wallpapers["green"]))
        ], check=True)
    if event.name == "f15":
        tappad.set_rgb(0,0,255,100)
        wizapi.send_config({"state": True,"dimming":70,"b":255})
        subprocess.run([
            str(we),
            "-control", "openWallpaper",
            "-file", str(Path(wallpapers["blue"]))
        ], check=True)
    if event.name == "f16":
        tappad.set_rgb(255,255,255,100)
        wizapi.send_config({"state": True,"dimming":100,"temp": 6500})
        subprocess.run([
            str(we),
            "-control", "openWallpaper",
            "-file", str(Path(wallpapers["white"]))
        ], check=True)
    if event.name == "f17":
        tappad.set_rgb(0,255,255,100)
        wizapi.send_config({"state": True,"dimming":70,"g":255,"b":255})
        os.startfile("D:\\Playnite")
    if event.name == "f18":
        current = sbc.get_brightness(display=0)
        sbc.set_brightness(current[0]-10)
    if event.name == "f19":
        current = sbc.get_brightness(display=0)
        sbc.set_brightness(current[0]+10)
    if keyboard.is_pressed("F20"):
        x += 1
        if x >= 40:
            x = 0
            tappad.set_rgb(0,0,0,0)
            wizapi.send_config({"state": False})
            subprocess.run(["shutdown", "/s", "/f", "/t", "0"])
    else:
        if x>=1 and x<5:
            webbrowser.open_new_tab("https://stardance.hackclub.com/home")
            x = 0