import numpy as np
import math

#==============================================================================#    
#------------------Implementação da matriz Jacobiana---------------------------#
#==============================================================================#



class jacobiano:
    def __init__(self, theta, barras, volt, tap, tipotap, Qcalc, Pcalc, tipobar, dP, dQ, G, B):
        
        self.theta = theta    
        self.barras = barras
        self.volt = volt
        self.Qcalc = Qcalc
        self.Pcalc = Pcalc
        self.tipobar = tipobar
        self.dP = dP
        self.dQ = dQ
        self.G = G
        self.B = B
        
    
        
#=============================================================================#
#                               funcao jacobiano                              #
#_____________________________________________________________________________#
    
    def jacobiano(self):
        
        H = np.zeros((self.barras,self.barras), dtype = float) 
        N = np.zeros((self.barras,self.barras), dtype = float) 
        M = np.zeros((self.barras,self.barras), dtype = float) 
        L = np.zeros((self.barras,self.barras), dtype = float) 
    
#-----Interações para montar as matrizes H N M L do jacobiano-----------------# 
        for p in range(self.barras):
            for q in range(self.barras):
              
                if (p == q):
                                    
                    H[p][p] = -(self.Qcalc[p][0] + self.volt[p][0] * self.volt[p][0] * self.B[p][p]) 
                    N[p][p] =  (1 / self.volt[p][0]) * (self.Pcalc[p][0] + self.volt[p][0] * self.volt[p][0] * self.G[p][p]) 
                    M[p][p] =  self.Pcalc[p][0] - (self.volt[p][0] * self.volt[p][0] * self.G[p][p]) 
                    L[p][p] =  (1 / self.volt[p][0]) * (self.Qcalc[p][0] - self.volt[p][0] * self.volt[p][0] * self.B[p][p]) 
            
                else:
            
                    tkm = self.theta[p][0] - self.theta[q][0]
            
                    H[p][q] =  self.volt[p][0] * self.volt[q][0]  * (self.G[p][q] * np.sin(tkm) - self.B[p][q] * np.cos(tkm))
                    N[p][q] =  self.volt[p][0] * (self.G[p][q] * np.cos(tkm) + self.B[p][q] * np.sin(tkm))
                    M[p][q] = -self.volt[p][0] * self.volt[q][0]  * (self.G[p][q] * np.cos(tkm) + self.B[p][q] * np.sin(tkm))
                    L[p][q] =  self.volt[p][0] * (self.G[p][q] * np.sin(tkm) - self.B[p][q] * np.cos(tkm))
            
            
#--------------------------------BIG NUMBER ----------------------------------#           
                 
           
        for j in range (self.barras):
            if (self.tipobar[j,0] == 2):
                H[j,j]=10**20
                L[j,j]=10**20
                self.dP[j,0]=0
                self.dQ[j,0]=0
                
                
            elif (self.tipobar[j,0] == 1):    
                L[j,j]=10**20
                self.dQ[j,0]=0
                       
                
#---------------------------Matriz Jacobiana----------------------------------#

        Jacobiano = np.zeros((2*self.barras,2*self.barras), dtype = float) 
         
            
           
        for jc in range (self.barras):
            for jl in range (self.barras):  
              
                Jacobiano[jc][jl] = H[jc][jl]
                Jacobiano[jc][jl+self.barras] = N[jc][jl]
                Jacobiano[jc+self.barras][jl] = M[jc][jl]
                Jacobiano[jc+self.barras][jl+self.barras] = L[jc][jl]
        
        return Jacobiano
        









