import cv2,math
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import pygame
pygame.init()

WIDTH = 500
HIEGHT = 450
window = pygame.display.set_mode((WIDTH,HIEGHT))

pygame.display.set_caption("Science Porject PLAZMA")
pygame.mixer.init()
pygame.mixer.music.load("F:\\Tirth\\filesa\\Science Projectt\\alert.wav")
SideViewCarRaw = pygame.image.load(r"F:\Tirth\filesa\Science Projectt\sideSeat.jpg")
sideCartMAin = pygame.transform.scale(SideViewCarRaw,(WIDTH,HIEGHT))
sleepingSign_Raw = pygame.image.load(r"F:\Tirth\filesa\Science Projectt\ZZ.jpg")
sleepingSign = pygame.transform.scale(sleepingSign_Raw,(300,300))
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []
color = (0,255,0)

maxBlackoutTime= 3

blackoutRunning = 0
minLighenTime = 1
LightenRunning=0
firstTime = True
isSlept = False
def findDistaceBetween2Points(p1,p2):
    x_len =  p1[0] - p2[0]
    y_len =  p1[1] - p2[1]
    dis = math.sqrt(x_len*x_len + y_len*y_len)
    return dis
def drawCar():
    window.blit(sideCartMAin,(0,0,WIDTH,HIEGHT))
    if isSlept:
        window.blit(sleepingSign,(220,25,200,200))
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            
            IsRunning = False
            break
    
    window.fill((0,0,0))
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=True)
    cv2.imshow("lo",img)
    drawCar()
    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 5,color, cv2.FILLED)

        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]
        lenghtVer= findDistaceBetween2Points(leftUp, leftDown)
        lenghtHor = findDistaceBetween2Points(leftLeft, leftRight)
        ratio = int((lenghtVer / lenghtHor) * 100)
        print(ratio)
        if(ratio < 38):
            a = 1*(25/1000) 
            blackoutRunning +=a
        else:
            firstTime = True
            blackoutRunning = 0
            isSlept = False
            pygame.mixer.music.stop()
        
    else:
        pass
        
    pygame.display.flip()