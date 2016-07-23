'''
Created on Jul 20, 2016
s
@author: User
'''
import pygame
import random
class noiseUtil:
    
    def __init__(self):
        self.GREEN = pygame.Color(0,153,51,255)
        self.BLUE = pygame.Color(0,32,128,255)
        self.RED = pygame.Color(255,0,0,255)
        self.BROWN = pygame.Color(255,150,100,255)
        self.WHITE = pygame.Color(255,255,255,255)
        self.YELLOW = pygame.Color(230,153,0,255)
        self.GRAY = pygame.Color(169,169,169,255)
        self.DARKGREEN = pygame.Color(51,102,0,255)
        self.LIGHTBLUE = pygame.Color(0,0,205,255)
        self.DARKBLUE = pygame.Color(0,0,150,255)
        self.PINK = pygame.Color(255,51,255,255) # A.k.a. "Debug Pink"
        
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
    
    def getGroundColor(self,size,heightMap,heatMap,moistureMap):
        colorArray = []
        for pos in range(size):
            colorArray.append([])
        for x in range(size):
            for y in range(size):
                if heightMap[x][y] < 0.3:
                    colorArray[x].append(self.BLUE)
                elif heightMap[x][y] < 0.37:
                    colorArray[x].append(self.DARKBLUE)
                elif heightMap[x][y] < 0.39:
                    colorArray[x].append(self.LIGHTBLUE)
                elif heightMap[x][y] > 0.4:
                    colorArray[x].append(pygame.Color(int(self.BROWN.r*heightMap[x][y]),int(self.BROWN.g*heatMap[x][y]),int(self.BROWN.b*heightMap[x][y])))
                else:
                    colorArray[x].append(self.YELLOW)
                '''elif (heightMap[x][y] > 0.95):
                    if (heatMap[x][y] < 0.95):
                        colorArray[x].append(self.GRAY)
                    if (heatMap[x][y] >= 0.95):
                        colorArray[x].append(self.WHITE)
                elif (heightMap[x][y] > 0.5):
                    if (heatMap[x][y] <= 0.85):
                        colorArray[x].append(self.GREEN)
                    if (heatMap[x][y] > 0.85):
                        colorArray[x].append(self.GRAY)
                elif (heightMap[x][y] > 0.4):
                    if(moistureMap[x][y] > 0.6):
                        if(heatMap[x][y] > 0.95):
                            colorArray[x].append(self.WHITE)
                        else:
                            colorArray[x].append(self.DARKGREEN)
                    if(moistureMap[x][y] <= 0.6):
                        if(heatMap[x][y] > 0.95):
                            colorArray[x].append(self.WHITE)
                        else:
                            colorArray[x].append(self.BROWN)
                            '''
                
                    
        return colorArray
        