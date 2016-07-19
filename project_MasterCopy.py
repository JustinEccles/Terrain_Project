import noise
import pygame
class noise_Gen2D:
    def __init__(self,scale,resolution=10,octaves=1,persistence=0.5,lacunarity=2.0,base=0.0):
        self.scale = scale
        self.resolution = resolution
        self.noiseList2D = []
        for pos in range(scale*resolution):
            self.noiseList2D.append([])
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.base = base
        
    def generate2DNoiseArray(self):
        for x in range(self.scale*self.resolution):
            for y in range(self.scale*self.resolution):
                newNoise = noise.snoise2(x/(self.scale*self.resolution),y/(self.scale*self.resolution),self.octaves,self.persistence,self.lacunarity,1024,1024,self.base)
                self.noiseList2D[x].append(newNoise)
        return self.noiseList2D
    def combineLayers(self,array1,weight1,array2,weight2):
        betaArray = []
        for pos in range(len(array1)):
            betaArray.append([])
        for x in range(len(array1)):
            for y in range(len(array1)):
                pntA = array1[x][y] * weight1
                pntB = array2[x][y] * weight2
                betaArray[x].append(pntA+pntB)
        return betaArray
    def sanitizePointList(self,pntArray):
        for x in range(len(pntArray)):
            for y in range(len(pntArray)):
                pnt = pntArray[x][y]
                pnt *= -1
                pnt *= 127
                pnt += 128
                pntArray[x][y] = pygame.Color(int(pnt),int(pnt),int(pnt))
        return pntArray           
    
