import mraa
import time
import math
import pygame

trigger = mraa.Gpio(32)
echo = mraa.Gpio(27)

trigger.dir(mraa.DIR_OUT)
echo.dir(mraa.DIR_IN)

D = 200
speed = 34000

pulse_start = time.time()
pulse_end = time.time()

print "Iniciando leitura ultrassom:"
time.sleep(3)
timeout=time.time()+D

while True:
    trigger.write(0)
    time.sleep(0.75)
    trigger.write(1)
    time.sleep(0.0001)
    trigger.write(0)
         
    
    while echo.read()==0:
        pulse_start = time.time()
                                
    while echo.read()==1:
        pulse_end=time.time()
           
    if echo.read()==0:            
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*speed/2
        distance=round(distance,0)
        print "Distancia:",distance,"cm"

        if distance < 10:
            print "Perto demais"
            pygame.init()
            pygame.mixer.music.load("ding.ogg")
            pygame.mixer.music.play()

    if time.time() > timeout:
        break
