'''
Created on Jul 18, 2016

@author: User
'''
import pygame
import time
from project_MasterCopy import noise_Gen2D
class Renderer:
    def __init__(self,noiseArray,size):
        self.noiseArray = noiseArray
        self.size = size
        res = (size,size)
        pygame.init()
        self.win = pygame.display.set_mode(res)
        self.pixelDisplay = pygame.Surface(res)
        self.copyPixelArrayToPixelDisplay(noiseArray)
        self.win.blit(self.pixelDisplay,(0,0))
        pygame.display.flip()
        pygame.image.save(self.win, "img1.png")
        while True:
            eventList = pygame.event.get()
            for even in eventList:
                if even.type == pygame.QUIT:
                    return
        
    def copyPixelArrayToPixelDisplay(self,pixelArrayList):
        for posX in range(self.size):
            for posY in range(self.size):
                self.pixelDisplay.set_at((posX, posY),pixelArrayList[posX][posY])

Ares = 256
Asize = 4
Alpha = noise_Gen2D(Asize,Ares,16,0.5,2.5,1.8)
Bravo = noise_Gen2D(Asize,Ares,16,0.8,10,0.0)
Beta = Alpha.generate2DNoiseArray()
Charlie = Bravo.generate2DNoiseArray()
Delta = Alpha.combineLayers(Beta, 0.8, Charlie, 0.2)
Gamma = Alpha.sanitizePointList(Delta)
Sigma = Renderer(Gamma,Asize*Ares)
