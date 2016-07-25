'''
Created on Jul 18, 2016

@author: User
'''
import time, math, pygame
from heatMap import heatMap
from cust_Perlin import cust_Perlin
from noiseUtil import noiseUtil
from random import seed
class Renderer:
    def __init__(self,noiseArray,size,name):
        self.size = size
        self.noiseArray = noiseArray
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





localtime = time.asctime( time.localtime(time.time()) )
print("Start: " + localtime)
noiseUtilities = noiseUtil()

seed = str(11) + ""
name = "11"
size = 12000
hMap = heatMap(size)
arrayHeat = hMap.getHeatMap()
perlAlpha = cust_Perlin(seed,size)
seed += seed
perlBravo = cust_Perlin(seed,size,)
seed += seed
perlCharlie = cust_Perlin(seed,size)
seed += seed
perlDelta = cust_Perlin(seed,size)
seed += seed
perlMoisture = cust_Perlin(seed,size)
arrayAlpha = []
arrayMoisture = []
for pos in range(size):
    arrayAlpha.append([])
    arrayMoisture.append([])

for x in range(size):
    for y in range(size):
        arrayMoisture[x].append(perlMoisture.custPerlOctave(x/120, y/120, 1, 0.8))
        tmpValue = abs(perlAlpha.custPerlOctave(x/(size/2), y/(size/2), 1, 0.5) - 0.25) * 0.5625
        tmpValue += abs(perlBravo.custPerlOctave(x/(size/5), y/(size/5), 2, 0.8) - 0.1) * 0.25
        tmpValue += abs(perlCharlie.custPerlOctave(x/(size/10), y/(size/10), 4, 0.8) - 0.025) * 0.125
        tmpValue += abs(perlDelta.custPerlOctave(x/(size/20), y/(size/20), 8, 0.8) - 0.01) * 0.0625
        arrayAlpha[x].append(tmpValue)
arrayOne = noiseUtilities.getGroundColor(size, arrayAlpha, arrayHeat, arrayMoisture)
localtime = time.asctime( time.localtime(time.time()) )
print("End: " + localtime)
Render_Alpha = Renderer(arrayOne,size,name + " biome")
#Render_Beta = Renderer(noiseUtilities.convertDblToClrArray(arrayHeat,noiseUtilities.RED, noiseUtilities.WHITE),size,name + " heat")
#Render_Charlie = Renderer(noiseUtilities.convertDblToClrArray(arrayMoisture,noiseUtilities.GRAY, noiseUtilities.BLUE),size,name + " moisture")
#Render_Delta = Renderer(noiseUtilities.convertDblToClrArray(arrayAlpha),size,name + " height")
'''ExperimentArray = []
for pos in range(size):
    ExperimentArray.append([])
for x in range(size):
    for y in range(size):
        ExperimentArray[x].append(pygame.Color(int(arrayOne[x][y].r * arrayAlpha[x][y]),int(arrayOne[x][y].g * arrayAlpha[x][y]),int(arrayOne[x][y].b * arrayAlpha[x][y])))
        
Render_Echo = Renderer(ExperimentArray,size,name + " bioheight")'''

