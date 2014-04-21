import numpy as np
from math import *
import matplotlib.pyplot as plt


#make sure you are in working directory, on Laptop  cd Documents/GitHub/Pterosaur
MAC=np.array([.532,.547,.556,.556,.556,.556,.556,.574,.574,.574,.574,.574,.574,.574,.574,.574,.574,.574,.574,.574,.574,.589,.589,.512])
#import data
class Wing:
    def __init__(self,num):
        self.data = np.loadtxt(fname='./Data/%d.txt' %num,skiprows=8, usecols=(1,11))#skips heading
        self.Cl,self.Xcp = self.data[:,0],self.data[:,1]
#from XFLR MAC for each wing
        
#N+1 is number of wings if importing all wings, wings start at 1 vs 0 in python
N=23
def GetWingData(N):
    wing = np.empty(N+1,dtype=object)
    for i in range(N):   
        wing[i+1]=Wing(i+1)
    return wing

wing=GetWingData(N)


xStart,xEnd = 0,1
yStart,yEnd = -1,1.1
size = 10
plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.grid(True)
plt.xlabel('Xcp',fontsize=16)
plt.ylabel('Cl',fontsize=16)
plt.xlim(xStart,xEnd)
plt.ylim(yStart,yEnd)
for i in range (N):
    plt.plot(wing[i+1].Cl,wing[i+1].Xcp/MAC[i])
