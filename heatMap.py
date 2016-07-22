'''
Created on Jul 22, 2016

@author: User
'''
import math as m
class heatMap:
     
    def __init__(self,size):
        self.arrayHeat = []
        for pos in range(size):
            self.arrayHeat.append([])
        
        for x in range(size):
            for y in range(size):
                tmpVal = m.sin(m.radians( (y*(410/size)-120 )))
                tmpVal *= -1
                tmpVal += 1
                tmpVal /= 2
                self.arrayHeat[x].append(tmpVal)
        
    def getHeatMap(self):
        return self.arrayHeat