import noise
class noise_Gen2D:
    def __init__(self,scale,resolution=10,octaves=1,persistence=0.5,lacunarity=2.0):
        self.scale = scale
        self.resolution = resolution
        self.noiseList2D = []
        for pos in range(scale*resolution):
            self.noiseList2D.append([])
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        
    def generate2DNoiseArray(self):
        for x in range(self.scale*self.resolution):
            for y in range(self.scale*self.resolution):
                newNoise = noise.snoise2(x/(self.scale*self.resolution),y/(self.scale*self.resolution),self.octaves,self.persistence,self.lacunarity)
                self.noiseList2D[x].append(newNoise)
        return self.noiseList2D
    def sanatisePointList(self,pntArray):
        for x in range(len(pntArray)):
            for y in range(len(pntArray)):
                pnt = pntArray[x][y]
                pnt *= 127
                pnt += 128
                pntArray[x][y] = int(pnt)
        return pntArray           
    
Alpha = noise_Gen2D(10,10,1)
Beta = Alpha.generate2DNoiseArray()
Gamma = Alpha.sanatisePointList(Beta)
for pos in range(Alpha.scale*Alpha.resolution):
    print(Gamma[pos])
