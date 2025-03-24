import numpy as np


class Ybus:
    def __init__(self, k, m, linhas, barras, bsh, tap, tipotap, Zlinha, shunt_bar):

        #variaveis
        self.linhas = linhas
        self.barras = barras
        self.k = k 
        self.m = m 
        self.bsh = bsh 
        self.tap = tap 
        self.tipotap = tap   
        self.Zlinha = Zlinha
        self.shunt_bar = shunt_bar
       
    def ybus(self):
#--------------------------Conversão do bsh para numero complexo--------------------------------#  
           
        BSH = np.zeros((self.linhas,1), dtype=complex)
        
        for bs in range (self.linhas):
             
            BSH[bs][0] = complex(0,self.bsh[bs][0])
        
            
#--------------------------Conversão do Z em Y--------------------------------#
        
        ykm = 1/self.Zlinha
                  

         
#-----------------------Dados tap transformador-------------------------------#
        '''
        tipo = 0 linha de transmissão
        tipo = 1 transformador de tap variavél 
        tipo = 2 transformador de tap fixo
        tipo = 3 transformador defasador
        tipo = 4 elemento shunt
        
        '''
        
#----------------------Construção da Ybus-------------------------------------#
            
        y = np.zeros((self.barras,self.barras), dtype=complex) 
        
        
#----------------Preenchimento da matriz bus------------------#
        
        for j in range(self.linhas):
            p=self.k[j,0]-1
            q=self.m[j,0]-1
            aux=complex (ykm[j,0]) 
            
            y[p][p] = y[p,p] + 1j*self.shunt_bar[p,0] #shunt da barra (banco de capacitores da subestação)
            
            if (self.tipotap[j,0] == 0):
                
                y[p,p]= y[p,p] + aux + (BSH[j,0])
            
                if(p!=q):
                    y[q,q]=y[q,q]+aux + (BSH[j,0])
                    y[p,q]=y[p,q]-aux
                    y[q,p]=y[p,q]
                
            elif (self.tipotap[j,0] != 0):
                y[p,p]=y[p,p]+aux*(self.tap[j,0]**2)
                y[q,q]=y[q,q]+aux
                y[p,q]=y[p,q]-aux*(self.tap[j,0])
                y[q,p]= y[p,q]
            
            
        return y

        
