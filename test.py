import numpy as np
from math import *
import matplotlib.pyplot as plt

class Wing:
    def __init__(self,sweep,wash,method):
        self.sweep=sweep
        self.wash=wash
        self.method=method
        
        #skiprows skips heading and usecols imports Cl and Xcp
    def XFLR5(self):    
        self.data = np.loadtxt(fname='C:/Users/Colin/Documents/GitHub/Pterosaur/WashData/'+self.method+self.sweep+self.wash+'.txt',skiprows=8, usecols=(1,11))
        self.Cl,self.Xcp = self.data[:,0],self.data[:,1]
        
wing[5outVLM1]=Wing[5,'out','VLM1']