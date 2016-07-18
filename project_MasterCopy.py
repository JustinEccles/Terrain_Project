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
            print("Row #" + str(x) + " being generated")
            for y in range(self.scale*self.resolution):
                newNoise = noise.snoise2(x/(self.scale*self.resolution),y/(self.scale*self.resolution),self.octaves,self.persistence,self.lacunarity,1024,1024,self.base)
                self.noiseList2D[x].append(newNoise)
        return self.noiseList2D
    def sanitizePointList(self,pntArray):
        for x in range(len(pntArray)):
            print("Row #" + str(x) + " being sanitized")
            for y in range(len(pntArray)):
                pnt = pntArray[x][y]
                pnt *= 127
                pnt += 128
                pntArray[x][y] = pygame.Color(int(pnt),int(pnt),int(pnt))
        return pntArray           
    
