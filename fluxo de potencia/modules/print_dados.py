

import numpy as np

class Print_dados:
    def __init__(self, theta, volt, barras, tipobar, linhas, Pkm, Qkm, k, m, iteracoes, estado):
        self.volt = volt 
        self.barras = barras
        self.tipobar = tipobar
        self.theta = theta
        self.linhas = linhas
        self.Pkm = Pkm
        self.Qkm = Qkm
        self.k = k
        self.m = m
        self.iteracoes = iteracoes
        self.estado = estado
        
    def print_fluxo(self):
        print("\nNúmero de iterações:", self.iteracoes,"\n")
        print("=============================================================\nVariáveis de estado\n=============================================================\n")
        print("\n{:<8} {:<15} {:<15} {:<30}".format('Barra', 'Tipo', 'V', 'Theta'))
        print("\n-------------------------------------------------------------\n")
        
        for pt in range(self.barras):
            print("{:<8} {:<15} {:<15} {:<30}".format(pt+1, self.tipobar[pt, 0], round(self.volt[pt, 0], 3), round(self.theta[pt, 0], 3)))
        
        print("\n\n\n\n=================================================================\nFluxo de carga\n=================================================================\n")
        print("{:<8} {:<15} {:<15} {:<15} {:<15}\n-------------------------------------------------------------\n".format('De', 'Para', 'Pkm (MW)', 'Qkm (Mvar)', 'Estado'))
        
        for fp in range(self.linhas):
            p = self.k[fp,] - 1
            q = self.m[fp,] - 1
            print("%1s %10s %18s %15s %12s" % (p+1, q+1, np.around(self.Pkm[p,q], 2), np.around(self.Qkm[p,q], 2), self.estado[fp]))
            



