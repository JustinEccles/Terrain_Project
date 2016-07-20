'''
Created on Jul 19, 2016

@author: User
'''
import random
class cust_Perlin:

    def __init__(self,seed,size=256,repeat=0):
        self.size = size
        self.seed = seed
        self.repeat = repeat
        self.randNum = random.Random()
        self.randNum.seed(self.seed)
        self.p = []
        for x in range(self.size):
            self.p.append(x)
        self.scramblePermutation()
        
    def scramblePermutation(self):
        self.randNum.shuffle(self.p)
        for x in range(self.size):
            self.p.append(self.p[x])
            
            
    def custPerl(self,x,y,z=0):
        if self.repeat > 0:
            x = x%self.repeat
            y = y%self.repeat
            z = z%self.repeat
        
        xi = int(x) & 255
        yi = int(y) & 255
        zi = int(z) & 255
        
        xf = x - int(x)
        yf = y - int(y)
        zf = z - int(z)
        
        u = self.noiseFade(xf)
        v = self.noiseFade(yf)
        w = self.noiseFade(zf)
        
        AAA = self.p[self.p[self.p[         xi ]+         yi ]+         zi ]
        ABA = self.p[self.p[self.p[         xi ]+self.inc(yi)]+         zi ]
        AAB = self.p[self.p[self.p[         xi ]+         yi ]+self.inc(zi)]
        ABB = self.p[self.p[self.p[         xi ]+self.inc(yi)]+self.inc(zi)]
        BAA = self.p[self.p[self.p[self.inc(xi)]+         yi ]+         zi ]
        BBA = self.p[self.p[self.p[self.inc(xi)]+self.inc(yi)]+         zi ]
        BAB = self.p[self.p[self.p[self.inc(xi)]+         yi ]+self.inc(zi)]
        BBB = self.p[self.p[self.p[self.inc(xi)]+self.inc(yi)]+self.inc(zi)]
        
        x1 = self.lerp(self.grad (AAA,xf, yf,zf),self.grad(BAA,xf-1, yf,zf),u);                                    
        x2 = self.lerp(self.grad (ABA, xf,yf-1,zf),self.grad(BBA,xf-1,yf-1,zf),u);
        y1 = self.lerp(x1, x2, v);
    
        x1 = self.lerp(self.grad(AAB,xf,yf,zf-1),self.grad(BAB,xf-1,yf,zf-1),u);
        x2 = self.lerp(self.grad(ABB,xf,yf-1,zf-1),self.grad(BBB,xf-1,yf-1,zf-1),u);
        y2 = self.lerp (x1, x2, v);
        
        return (self.lerp(y1,y2,w)+1)/2
        
        
    def lerp(self,a,b,x):
        return a + (x * (b - a))
        
    def grad(self,hashed,x,y,z):
        h = hashed & 15
        u = x if h < 8 else y
        if h < 4:
            v = y
        elif h == 12 or h == 14:
            v = x
        else:
            v = z
        return (u if ((h&1) == 0) else -u) + (v if ((h&2) == 0) else -v)
        
        
    def noiseFade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)
    
    
    def inc(self,a):
        a += 1
        if self.repeat > 0:
            a %= self.repeat
        return a
    
    
    
