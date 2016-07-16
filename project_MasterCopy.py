import noise

noiseList = []
noiseList2D = []
for x in range(10):
    for y in range(10):
        newNoise = noise.snoise2(x,y,1,0.5,2.0)
        noiseList.append(newNoise)
    noiseList2D.append(noiseList)

    
print(noiseList2D)