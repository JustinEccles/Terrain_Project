'''
Created on Jul 20, 2016
s
@author: User
'''
import pygame
class noiseUtil:
    
    def __init__(self):
        name = ""
        
    def convertDblToClrArray(self,colorArray,blackReplace=pygame.Color(0,0,0,255),whiteReplace=pygame.Color(255,255,255,255)):
        RGRat = (whiteReplace.r - blackReplace.r)/255
        GGRat = (whiteReplace.g - blackReplace.g)/255
        BGRat = (whiteReplace.b - blackReplace.b)/255
        for posX in range(len(colorArray)):
            for posY in range(len(colorArray)):
                tmpVal = colorArray[posX][posY]
                tmpR,tmpG,tmpB = None,None,None
                if RGRat < 0:
                    tmpR = 255 + (int(tmpVal * RGRat * blackReplace.r))
                else:
                    tmpR = int(tmpVal * RGRat * whiteReplace.r) + blackReplace.r
                if GGRat < 0:
                    tmpG = 255 + (int(tmpVal * GGRat * blackReplace.g))
                else:
                    tmpG = int(tmpVal * GGRat * whiteReplace.g) + blackReplace.g
                if BGRat < 0:
                    tmpB = 255 + (int(tmpVal * BGRat * blackReplace.b))
                else:
                    tmpB = int(tmpVal * BGRat * whiteReplace.b) + blackReplace.b
                colorArray[posX][posY] = pygame.Color(tmpR,tmpG,tmpB,255)
                
        return colorArray
                