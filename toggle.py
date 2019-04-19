from tkinter import *
import tkinter .font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
## Hardware
red_led = LED(17)
blue_led = LED(22)
green_led = LED(27)

## GUI Definitions
## New window called win and title for that window
win = Tk()
win.title("LED Toggler")
#set a font for items in the future, note weight sets the font as bold
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

def redToggle():
    if red_led.is_lit:
        red_led.off()
        redButton["text"] = "Turn red ON"
    else:
        red_led.on()
        green_led.off()
        blue_led.off()
        redButton["text"] = "Turn red OFF"
def greenToggle():
    if green_led.is_lit:
        green_led.off()
        greenButton["text"] = "Turn green ON"
    else:
        green_led.on()
        red_led.off()
        blue_led.off()
        greenButton["text"] = "Turn green OFF"
def blueToggle():
    if blue_led.is_lit:
        blue_led.off()
        blueButton["text"] = "Turn blue ON"
    else:
        blue_led.on()
        green_led.off()
        red_led.off()
        blueButton["text"] = "Turn blue OFF"
        
def exitToggle():
    quit()
        
##Widgets
redButton = Button(win, text = "Turn red On", font = myFont, command = redToggle, bg = "bisque2", height = 1, width = 24)
redButton.grid(row=0, column = 1)

greenButton = Button(win, text = "Turn green On", font = myFont, command = greenToggle, bg = "bisque2", height = 1, width = 24)
greenButton.grid(row = 1, column = 1)

blueButton = Button(win, text = "Turn blue On", font = myFont, command = blueToggle, bg = "bisque2", height = 1, width = 24)
blueButton.grid(row = 2, column = 1)

exitButton = Button(win, text = "Exit Program", font = myFont, command = exitToggle, bg = "bisque2", height =1, width =24)
exitButton.grid(row = 3, column = 1) 