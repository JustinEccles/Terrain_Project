import noise
size = 10
noiseList2D = []
for pos in range(size):
    noiseList2D.append([])
x,y = 0,0
for x in range(size):
    for y in range(size):
        newNoise = noise.snoise2(x/size,y/size,1,0.5,2.0)
        noiseList2D[x].append(newNoise)
    

for pos in  noiseList2D:
    print(pos)