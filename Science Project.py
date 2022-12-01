import pygame
import time

import serial
arduinoData = serial.Serial('COM4', 115200)
time.sleep(1)
ControllCar = False
pygame.init()
WIDTH = 1500
HIEGHT = 700
window = pygame.display.set_mode((WIDTH,HIEGHT))
pygame.display.set_caption("Science Porject PLAZMA")
IsRunning = True
blueCar_raw = pygame.image.load(r".\blueCar.jpg")
blueCar = pygame.transform.rotate(pygame.transform.scale(blueCar_raw,(150,150)),-90)
redCar_raw = pygame.image.load(r"\redCat.jpg")
redCar = pygame.transform.rotate(pygame.transform.scale(redCar_raw,(130,120)),90)
RED = (255, 0, 39)
WHITE = (255,255,255)
objectColor = (250,0,0)
FontColor = (0,0,0)
myCarWidth = 50
myCarBottom = 50
Cxwidth = 45
distances =[]
BGColor = WHITE
ConstantAcceler = 10
Padding = 100
F_Size = 45
FirstTimesound = False
font = pygame.font.Font('freesansbold.ttf', 16)
pygame.mixer.music.load(r".\alert.wav")
FirstTimesound = True
safeDistanceRange = 12
def Draw_objects():
    #MyCar
    EachSidePos = [
    (WIDTH/2 -Cxwidth,HIEGHT-(myCarBottom+myCarWidth*2+distances[0]+250)/2,Cxwidth*2,Cxwidth*2),
    (WIDTH/2 -Cxwidth - distances[1],HIEGHT-((myCarWidth*2) + myCarBottom),Cxwidth*2,Cxwidth*2),
    (WIDTH/2 +Cxwidth + distances[2],HIEGHT-((myCarWidth*2) + myCarBottom),Cxwidth*2,Cxwidth*2)
    ]
    
    pygame.draw.rect(window,(0,0,200),(WIDTH/2 - myCarWidth,HIEGHT-((myCarWidth*2) + myCarBottom),myCarWidth*2,myCarWidth*2))
    #images Axis Object
    window.blit(redCar,EachSidePos[0])
    window.blit(redCar,EachSidePos[1])
    window.blit(redCar,EachSidePos[2])
    global BGColor

    if(distances[0]/ConstantAcceler < safeDistanceRange and FirstTimesound):
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.pause()
    # draws Axis Object

    #pygame.draw.rect(window,objectColor,EachSidePos[0])
    #pygame.draw.rect(window,objectColor,EachSidePos[1])
    #pygame.draw.rect(window,objectColor,EachSidePos[2])

    window.blit(blueCar,(WIDTH/2 - myCarWidth,HIEGHT-((myCarWidth*2) + myCarBottom),myCarWidth*2,myCarWidth*2))
    window.blit((font.render(str(distances[0]/ConstantAcceler), True, FontColor)),(WIDTH/2 - myCarWidth,300,F_Size,F_Size))
    window.blit((font.render(str(distances[1]/ConstantAcceler), True, FontColor)),(WIDTH/2-100,HIEGHT-((myCarWidth*2) + myCarBottom),F_Size,F_Size))
    window.blit((font.render(str(distances[2]/ConstantAcceler), True, FontColor)),(WIDTH/2+100,HIEGHT-((myCarWidth*2) + myCarBottom),F_Size,F_Size))

while IsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            IsRunning = False
            break
    window.fill(BGColor)
    while arduinoData.inWaiting() == 0:
        pass
    
    datapack = arduinoData.readline()
    stringedPack = datapack.decode()
    stringedPack_arr = stringedPack.split("ALN")
    for i in range(len(stringedPack_arr)):
        stringedPack_arr[i] = float(stringedPack_arr[i])
    distances=[round(stringedPack_arr[0])*ConstantAcceler,round(stringedPack_arr[1])*ConstantAcceler,round(stringedPack_arr[2])*ConstantAcceler]
    Draw_objects()
    pygame.display.flip()