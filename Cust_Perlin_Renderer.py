'''
Created on Jul 18, 2016

@author: User
'''
import pygame
import math
from cust_Perlin import cust_Perlin
from noiseUtil import noiseUtil
class Renderer:
    def __init__(self,noiseArray,size,name):
        self.noiseUtilities = noiseUtil()
        self.size = size
        self.noiseArray = self.noiseUtilities.convertDblToClrArray(noiseArray)
        self.name = str(name)
        res = (size,size)
        pygame.init()
        self.win = pygame.display.set_mode(res)
        self.pixelDisplay = pygame.Surface(res)
        self.copyPixelArrayToPixelDisplay(noiseArray)
        self.win.blit(self.pixelDisplay,(0,0))
        pygame.display.flip()
        pygame.image.save(self.win, self.name + ".png")
        while True:
            eventList = pygame.event.get()
            for even in eventList:
                if even.type == pygame.QUIT:
                    return
                
    def copyPixelArrayToPixelDisplay(self,pixelArrayList):
        for posX in range(self.size):
            for posY in range(self.size):
                self.pixelDisplay.set_at((posX, posY),pixelArrayList[posX][posY])
        
Size_Alpha = 1000
Array_Alpha = []
Seed_Alpha = 420
Perl_Alpha = cust_Perlin(Seed_Alpha,Size_Alpha,0)
for pos in range(Size_Alpha):
    Array_Alpha.append([])
for x in range(Size_Alpha):
    for y in range(Size_Alpha):
        Array_Alpha[x].append(Perl_Alpha.custPerl(x/math.sqrt(Size_Alpha), y/math.sqrt(Size_Alpha)))
Render_Alpha = Renderer(Array_Alpha,Size_Alpha,Seed_Alpha)


