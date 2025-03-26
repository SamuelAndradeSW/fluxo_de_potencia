
import numpy as np
import math
from modules.jacobiano2 import jacobiano
from modules.anarede2python import Anarede2Python 
from modules.Ybus_trabalho1 import Ybus
from modules.print_dados import Print_dados

DADOS = Anarede2Python("fluxo de potencia/data/IEEE14-BARRAS.pwf")

arquivo = open('Resultados.txt', 'w')
#--------------------------inicialização dos dados----------------------------#

linhas = DADOS.contador_Linhas
barras = DADOS.contador_Barras
k = DADOS.BARRA_DE
m = DADOS.BARRA_PARA
tap = DADOS.tap
tipotap = DADOS.Tipo_Elemento
bsh = DADOS.B_shunt
tipobar = DADOS.Tipo_Barra
Zlinha_aux = DADOS.Z_lin



#-------------------- dados de barra


shunt_bar = DADOS.Shunt_Barra/100 #divide por 100 pois os dados estão em PU
QGER = DADOS.Qger_Barra/100
Q = DADOS.Qcarga_Barra/100
POT_ger = DADOS.Pger_Barra/100
POT = DADOS.Pcarga_Barra/100

estado_aux = np.ones(linhas)

Zlinha = np.copy(Zlinha_aux)

for s in range(linhas):
    
    if (tipotap[s,0] == 0):
    
        estado = np.copy(estado_aux)
        estado[s,] = estado[s,] * 0
        
        if (estado[s,] == 0): 
            
            Zlinha[s,0] = (10**20) * Zlinha[s,0]  

            ybus = Ybus( k, m, linhas, barras, bsh, tap, tipotap, Zlinha, shunt_bar).ybus()
            
            
            
            G = np.zeros((barras,barras), dtype = float)  
            B = np.zeros((barras,barras), dtype = float)  
            
            for i in range (barras):
                for j in range (barras):
                    G[i,j]= ybus.real[i,j]
                    B[i,j]= ybus.imag[i,j]
            
            
            
                    
            #-----------------------------------------------------------------------------#
            #                               MÉTODO DE NEWTON-RAPHSON                      #
            #_____________________________________________________________________________#
            
            
            erro = 10**(-3)
            aux = 0
            
            iteracoes = -1
            while (aux != 1 and iteracoes < 100):
            
                iteracoes += 1
            #----------- DADOS------------------------------------------------------------#
                
                theta = DADOS.Angulo_Barra
                volt = DADOS.Tensao_Barra
                
                Qesp = (QGER - Q)
                Pesp = (POT_ger - POT)
                
                
                Vcomplex = volt*np.exp(1j*theta)               # Tensao na barra em magnitude e fase;
                I           = np.matmul(ybus, Vcomplex)        # Corrente injetada na barra;
                
                Scalc    = Vcomplex * np.conj(I)               # Potencia aparente calculada;
                Pcalc    = Scalc.real                          # Potencia ativa calculada;
                Qcalc    = Scalc.imag                          # Potencia reativa calculada;
                
                dP   = (Pesp - Pcalc)                     
                dQ   = (Qesp - Qcalc)                       
                
                jac = jacobiano(theta, barras, volt, tap, tipotap, Qcalc, Pcalc, tipobar, dP, dQ, G, B).jacobiano()
                      
                  
                
                DeltaY   = np.concatenate((dP, dQ))
            #-----------------------------------------------------------------------------#   
               
                DeltaX = np.matmul(np.linalg.inv(np.asmatrix(jac)), DeltaY)
            
                for jj in range (barras):
                    theta[jj][0] = theta[jj][0] + DeltaX[jj][0]
                    volt[jj][0] = volt[jj][0] + DeltaX[barras+jj][0]
                    
                
                if (np.abs(DeltaY).max()<erro):
                    
                    aux = 1
                    
                    
            
            P_gerado   = (Pcalc + POT)*100                     
            Q_gerado   = (Qcalc + Q)*100  
            
            tensao = volt
            thetaD = theta*(180/np.pi)
            
            #=============================================================================#
            #                         Fluxo de potencia                                   #
            #_____________________________________________________________________________#
            
                  
            Pkm = np.zeros((barras,barras), dtype = float)
            Qkm = np.zeros((barras,barras), dtype = float)
            
            aux1 = np.zeros((barras,barras), dtype = float)
            aux2 = np.zeros((barras,barras), dtype = float)
             
            #tap2 = DADOS.
                                                                       
            for fp in range(linhas):
                
                p = k[fp,0]-1
                q = m[fp,0]-1
                tkm=theta[p,0]-theta[q,0]
                Bsh = bsh[fp,0]
                Vk=volt[p,0]
                Vm=volt[q,0]
                a = tap[fp][0]
                
                
                #linha de transmissão
                if (tipotap[fp,0] == 0):
                          
                    Pkm[p,q] = -((Vk**2)*G[p,q] - Vk*Vm*G[p,q]*math.cos(tkm) - Vk*Vm*B[p,q]*math.sin(tkm))*100
                    Qkm[p,q] =  -(-(Vk**2)*(B[p,q] - (Vk**2)*Bsh) + Vk*Vm*B[p,q]*math.cos(tkm) -  Vk*Vm*G[p,q]*math.sin(tkm))*100
                    aux1[p,q] = Pkm[p,q]
                    aux2[p,q] = Qkm[p,q]
                    
                #trafo em fase  
                elif (tipotap[fp,0] == 2):
                        
                    Pkm[p,q] =  -((a**2)*(Vk**2)*G[p,q] - a*Vk*Vm*G[p,q]*math.cos(tkm) - a*Vk*Vm*B[p,q]*math.sin(tkm))*100
                    Qkm[p,q] =   -(-(a**2)*(Vk**2)*B[p,q] + (a*Vk*Vm*B[p,q]*math.cos(tkm) - a*Vk*Vm*G[p,q]*math.sin(tkm)))*100
            
        
            De = k[s]
            para = m[s]
            print("\n","\n","linha removida:", s,"\n", 'De', De, 'Para', para, "\n") 
    
            relatorio = Print_dados(theta, volt, barras, tipobar, linhas, Pkm, Qkm, k, m, iteracoes, estado).print_fluxo()
             
            Zlinha[s,0] =  Zlinha_aux[s,0]  
    
    




                    
                
        
    

        
        


        
     

    
    
  

 

        

        






































       
        
        