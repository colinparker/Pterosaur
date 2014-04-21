import numpy as np
from math import *
import matplotlib.pyplot as plt


#make sure you are in working directory, on Laptop  cd Documents/GitHub/Pterosaur

#import data
class Wing:
    def __init__(self,num):
        self.data = np.loadtxt(fname='../Pterosaur/%d.txt' %num,skiprows=8, usecols=(1,11))#skips heading
        self.Cl,self.Xcp = self.data[:,0],self.data[:,1]
        
#N+1 is number of wings if importing all wings, wings start at 1 vs 0 in python
N=23 

wing = []
#move index up 1 to match wing number in XFLR
wing.append(0) 
for i in range(N):
    
    wing.append(Wing(i+1))

