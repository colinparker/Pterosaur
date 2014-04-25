import numpy as np
from math import *
import matplotlib.pyplot as plt
from IPython.display import Latex as la

dir = './WashData/'
#dir='C:/Users/Colin/Documents/GitHub/Pterosaur/WashData/'
class Wing:
    def __init__(self,sweep,wash,method):
        self.sweep=sweep
        self.wash=wash
        self.method=method
        
        #skiprows skips heading and usecols imports Cl and Xcp    
        self.data = np.loadtxt(fname=dir+self.method+self.sweep+self.wash+'.txt',skiprows=8, usecols=(1,11))
        self.Cl,self.Xcp = self.data[:,0],self.data[:,1]
    def plot(self,color,line):
        xStart,xEnd = 0,1
        yStart,yEnd = -1,1.5
        size = 10
        plt.title('Effects of Flexability')
        plt.grid(True)
        plt.xlabel('Xcp as %MAC',fontsize=16)
        plt.ylabel('Cl',fontsize=16)
        plt.xlim(xStart,xEnd)
        plt.ylim(yStart,yEnd)
        plt.plot(self.Xcp,-self.CL,color,ls=line,lw=2)
        
MAC=.556

wing={}

def GetWing(sweep,wash,method):
   
    wing[sweep+wash+method]=Wing(sweep,wash,method)

GetWing('25','out','VLM1')
GetWing('5','out','VLM1')
GetWing('10','out','VLM1')
GetWing('0','in','VLM1')
GetWing('25','in','VLM1')
GetWing('5','in','VLM1')
GetWing('10','in','VLM1')
GetWing('25','out','VLM2')
GetWing('5','out','VLM2')
GetWing('10','out','VLM2')
GetWing('0','in','VLM2')
GetWing('25','in','VLM2')
GetWing('5','in','VLM2')
GetWing('10','in','VLM2')
GetWing('25','out','PANEL')
GetWing('5','out','PANEL')
GetWing('10','out','PANEL')
GetWing('0','in','PANEL')
GetWing('25','in','PANEL')
GetWing('5','in','PANEL')
GetWing('10','in','PANEL')
GetWing('25','out','LLT')
GetWing('5','out','LLT')
GetWing('10','out','LLT')
GetWing('0','in','LLT')
GetWing('25','in','LLT')
GetWing('5','in','LLT')
GetWing('10','in','LLT')