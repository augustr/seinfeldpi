#!/usr/bin/env python
import time
import pygame
import RPi.GPIO as GPIO
import glob
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 4

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

pygame.mixer.init()

# Create only one channel for audio
channel = pygame.mixer.Channel(0)

# Load all audio files
audio_files = glob.glob("./audio/*.wav")

audios = []
for audio_file in audio_files:
    print "Registering audio file: " + audio_file
    audios.append(pygame.mixer.Sound(audio_file))

def play_random():
    if audios:
        print "Playing"
        p = random.choice(audios)
        if not channel.get_busy():
            channel.play(p)

def stop():
    channel.stop()

# Start sensing
door = False

print "Seinfeld door sensor started"

while True:
    button_state = GPIO.input(button)
    if button_state == GPIO.HIGH:
    #if False:
        if door == True:
            print "Door close"
            #stop()
        door = False
    else:
        if door == False:
            print "Door open, playing seinfeld bass solo!"
            play_random()
        door = True
    time.sleep(0.1)