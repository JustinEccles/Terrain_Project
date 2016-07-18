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
        print("Copying pixels by hand")
        self.copyPixelArrayToPixelDisplay(noiseArray)
        self.win.blit(self.pixelDisplay,(0,0))
        print("Displaying Heightmap")
        pygame.display.flip()
        while True:
            eventList = pygame.event.get()
            for even in eventList:
                if even.type == pygame.QUIT:
                    return
        
    def copyPixelArrayToPixelDisplay(self,pixelArrayList):
        for posX in range(self.size):
            print("Row #" + str(posX) + " being copied")
            for posY in range(self.size):
                self.pixelDisplay.set_at((posX, posY),pixelArrayList[posX][posY])

    
Asize = 60
Ares = 10
Alpha = noise_Gen2D(Asize,Ares,2,0.4,7)
print("Generating Array")
Beta = Alpha.generate2DNoiseArray()
print("Sanitizing Array")
Gamma = Alpha.sanitizePointList(Beta)
print("Rendering Display")
Sigma = Renderer(Gamma,Asize*Ares)
