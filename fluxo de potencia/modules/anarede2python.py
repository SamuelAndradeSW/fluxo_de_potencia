import os
import numpy as np


class Anarede2Python(object):

    encode = 'utf-8'

    def __init__(self, diretorio):
        # Resgatando caminho do arquivo .pwf definido pelo usuario
        self.diretorio = diretorio

        # Contando numero de barras e linhas do sistema
        with open(self.diretorio, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Contando numero de barras
                if linha.strip() == 'DBAR':
                    next(arquivo)  # Tem que pular a linha do cabecalho
                    linha_aux = next(arquivo)
                    self.contador_Barras = 0
                    while linha_aux.strip() != '99999':
                        linha_aux = next(arquivo)
                        self.contador_Barras += 1

                # Contando numero de linhas
                if linha.strip() == 'DLIN':
                    next(arquivo)  # Tem que pular a linha do cabecalho
                    linha_aux = next(arquivo)
                    self.contador_Linhas = 0
                    while linha_aux.strip() != '99999':
                        linha_aux = next(arquivo)
                        self.contador_Linhas += 1

        # Inicializando as variaveis de barra do sistema
        # numero da barra
        self.BARRA = np.zeros((self.contador_Barras,1), dtype=int)
        # operacao da barra
        self.Operacao_Barra = list()
        # estado da barra
        self.Estado_Barra = list()
        # tipo da barra
        self.Tipo_Barra = np.zeros((self.contador_Barras,1), dtype=int)
        # grupo base de tensao
        self.Grupo_Base_Tensao_Barra = list()
        # nome da barra
        self.Nome_Barra = list()
        # grupo limite de tensao
        self.Grupo_Lim_Tensao_Barra = list()
        # tensao
        self.Tensao_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # angulo
        self.Angulo_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # geracao ativa
        self.Pger_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # geracao reativa
        self.Qger_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # geracao reativa minima
        self.Qger_min_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # geracao reativa maxima
        self.Qger_max_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # barra controlada
        self.Barra_Controlada = list()
        # carga ativa
        self.Pcarga_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # carga reativa
        self.Qcarga_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # componente shunt(capacitor, reator)
        self.Shunt_Barra = np.zeros((self.contador_Barras,1), dtype=float)
        # area
        self.Area_Barra = np.zeros((self.contador_Barras,1), dtype=int)

        # Inicializando as variaveis de linha do sistema
        # barra de
        self.BARRA_DE = np.zeros((self.contador_Linhas,1), dtype=int)
        # abertura da barra de
        self.Abertura_Barra_De = list()
        # operacao
        self.Operacao_Linha = list()
        # abertura da barra para
        self.Abertura_Barra_Para = list()
        # barra para
        self.BARRA_PARA = np.zeros((self.contador_Linhas,1), dtype=int)
        # numero circuito da linha
        self.Circuito_linha = np.zeros((self.contador_Linhas,1), dtype=int)
        # estado
        self.Estado_Linha = list()
        # proprietario linha
        self.Proprietario_Linha = list()
        # resistencia do circuito em %
        self.R_lin = np.zeros((self.contador_Linhas,1), dtype=float)
        # reatancia do circuito em %
        self.X_lin = np.zeros((self.contador_Linhas,1), dtype=float)
        # valor total da susceptancia shunt do circuito em Mvar
        self.B_shunt = np.zeros((self.contador_Linhas,1), dtype=float)
        # tap do transformador referido a barra de
        self.tap = np.zeros((self.contador_Linhas,1), dtype=float)
        # valor minimo para o tap
        self.Tap_Min = np.zeros((self.contador_Linhas,1), dtype=float)
        # valor maximo para o tap
        self.Tap_Max = np.zeros((self.contador_Linhas,1), dtype=float)
        # defasagem do transformador defasador
        self.fase = np.zeros((self.contador_Linhas,1), dtype=float)
        # o numero da barra a ter a tensao controlado pelo trafo com tap
        self.Barra_Ctrl_tap = np.zeros((self.contador_Linhas,1), dtype=int)
        # capacidade normal da linha
        self.Capacidade_Normal_Linha = np.zeros((self.contador_Linhas,1), dtype=float)
        # capacidade de emergencia da linha
        self.Capacidade_Emergencia_Linha = np.zeros((self.contador_Linhas,1), dtype=float)
        # numero de taps
        self.Numero_de_taps = np.zeros((self.contador_Linhas,1), dtype=int)
        # Parametros adicionais calculados com valores lidos
        # impedancia
        self.Z_lin = np.zeros((self.contador_Linhas,1), dtype=complex)
        # admitancia
        self.Admitancia_Linha = np.zeros((self.contador_Linhas,1), dtype=complex)
        # Tipo de linha
        self.Tipo_Elemento = np.zeros((self.contador_Linhas,1), dtype=int)

        # Realizando a leitura dos dados de linha e de barra do sistema
        self.leitura_dbar()
        self.leitura_dlin()

    # Metodos para leitura dos dados
    # Dados das Barras
    def leitura_dbar(self):
        with open(self.diretorio, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Identificacao do Sistema
                if linha.strip() == 'TITU':
                    print('Leitura dos dados de barra do sistema', next(arquivo)[:].strip())
                # Leitura dos dados
                if linha.strip() == 'DBAR':
                    next(arquivo)  # Tem que pular a linha do cabecalho
                    linha_atual = next(arquivo)
                    aux = 0
                    while linha_atual.strip() != '99999':
                        # numero da barra
                        self.BARRA[aux] = int(linha_atual[0:5].strip())
                        # operacao da barra
                        self.Operacao_Barra.append(str(linha_atual[5:6].strip()))
                        # estado da barra
                        self.Estado_Barra.append(str(linha_atual[6:7].strip()))
                        # tipo da barra
                        if linha_atual[7:8].strip() != '':  # posicao vazia significa barra do tipo 0
                            self.Tipo_Barra[aux] = int(linha_atual[7:8].strip())
                        # grupo base de tensao
                        self.Grupo_Base_Tensao_Barra.append(str(linha_atual[8:10].strip()))
                        # nome da barra
                        self.Nome_Barra.append(str(linha_atual[10:21].strip()))
                        # grupo limite de tensao
                        self.Grupo_Lim_Tensao_Barra.append(str(linha_atual[21:23].strip()))
                        # tensao ja em pu ???Divide pelo valor de VF????
                        self.Tensao_Barra[aux] = float(linha_atual[23:28].strip())/1000
                        # angulo
                        self.Angulo_Barra[aux] = float(linha_atual[28:32].strip())*np.pi/180
                        # geracao ativa ainda nao esta em pu
                        if linha_atual[32:37].strip() != '':  # posicao vazia significa que nao ha geracao PG=0
                            self.Pger_Barra[aux] = float(linha_atual[32:37].strip())
                        # geracao reativa ainda nao esta em pu
                        if linha_atual[37:42].strip() != '':  # posicao vazia significa que nao ha geracao QG=0
                            self.Qger_Barra[aux] = float(linha_atual[37:42].strip())
                        # geracao reativa minima
                        if linha_atual[42:47].strip() != '':  # posicao vazia significa que nao ha geracao QG=0
                            self.Qger_min_Barra[aux] = float(linha_atual[42:47].strip())
                        # geracao reativa maxima
                        if linha_atual[47:52].strip() != '':  # posicao vazia significa que nao ha geracao QG=0
                            self.Qger_max_Barra[aux] = float(linha_atual[47:52].strip())
                        # barra controlada
                        self.Barra_Controlada.append(str(linha_atual[52:58].strip()))
                        # carga ativa
                        if linha_atual[58:63].strip() != '':  # posicao vazia significa que nao ha geracao PL=0
                            self.Pcarga_Barra[aux] = float(linha_atual[58:63].strip())
                        # carga reativa
                        if linha_atual[63:68].strip() != '':  # posicao vazia significa que nao ha geracao QL=0
                            self.Qcarga_Barra[aux] = float(linha_atual[63:68].strip())
                        # componente shunt(capacitor, reator)
                        if linha_atual[68:73].strip() != '':  # posicao vazia significa que nao ha Shunt
                            self.Shunt_Barra[aux] = float(linha_atual[68:73].strip())
                        # area
                        self.Area_Barra[aux] = int(linha_atual[73:76].strip())
                        # Falta Vf??????????????????

                        # Pula para a proxima linha
                        linha_atual = next(arquivo)
                        aux += 1

        # Imprime os dados lidos
        # print(self.BARRA)
        # print(self.Operacao_Barra)
        # print(self.Estado_Barra)
        # print(self.Tipo_Barra)
        # print(self.Grupo_Base_Tensao_Barra)
        # print(self.Nome_Barra)
        # print(self.Grupo_Lim_Tensao_Barra)
        # print(self.Tensao_Barra)
        # print(self.Angulo_Barra)
        # print(self.Pger_Barra)
        # print(self.Qger_Barra)
        # print(self.Qger_min_Barra)
        # print(self.Qger_max_Barra)
        # print(self.Barra_Controlada)
        # print(self.Pcarga_Barra)
        # print(self.Qcarga_Barra)
        # print(self.Shunt_Barra)
        # print(self.Area_Barra)

    # Dados das linhas
    def leitura_dlin(self):
        with open(self.diretorio, 'r', encoding='utf-8') as arquivo:

            for linha in arquivo:
                # Identificacao do Sistema
                if linha.strip() == 'TITU':
                    print('Leitura dos dados de linha do sistema', next(arquivo)[:].strip())
                # Leitura dos dados
                if linha.strip() == 'DLIN':
                    next(arquivo)  # Tem que pular a linha do cabecalho
                    linha_atual = next(arquivo)
                    aux = 0
                    while linha_atual.strip() != '99999':
                        # barra de
                        self.BARRA_DE[aux] = int(linha_atual[0:5].strip())
                        # abertura da barra de
                        self.Abertura_Barra_De.append(str(linha_atual[5:6].strip()))
                        # operacao
                        self.Operacao_Linha.append(str(linha_atual[7:8].strip()))
                        # abertura da barra para
                        self.Abertura_Barra_Para.append(str(linha_atual[9:10].strip()))
                        # barra para
                        self.BARRA_PARA[aux] = int(linha_atual[10:15].strip())
                        # circuito da barra
                        self.Circuito_linha[aux] = int(linha_atual[15:17].strip())
                        # estado linha
                        self.Estado_Linha.append(str(linha_atual[17:18].strip()))
                        # proprietario linha
                        self.Proprietario_Linha.append(str(linha_atual[18:19].strip()))
                        # resistencia do circuito em %
                        if linha_atual[20:26].strip() != '':  # posicao vazia significa R=0
                            self.R_lin[aux] = float(linha_atual[20:26].strip())
                        # reatancia do circuito em %
                        if linha_atual[26:32].strip() != '':  # posicao vazia significa X=0
                            self.X_lin[aux] = float(linha_atual[26:32].strip())
                        # valor total da susceptancia shunt do circuito em Mvar
                        if len(linha_atual) > 32 and linha_atual[32:38].strip() != '':
                            # Arquivo pode nao ter essas informacoes???posicao vazia significa Suceptancia=0
                            self.B_shunt[aux] = float(linha_atual[32:38].strip())
                        # tap do transformador referido a barra de
                        if len(linha_atual) > 38 and linha_atual[38:43].strip() != '':
                            # Arquivo pode nao ter essas informacoes???posicao vazia significa tap=0
                            self.tap[aux] = 1/float(linha_atual[38:43].strip())
                            # No anarede valor vem como sendo a:1, por isso inverte para ficar como 1:a
                        # valor minimo para o tap
                        if len(linha_atual) > 43 and linha_atual[43:48].strip() != '':
                            # Arquivo pode nao ter essas informacoes???posicao vazia significa min tap=0
                            self.Tap_Min[aux] = float(linha_atual[43:48].strip())
                        # valor maximo para o tap
                        if len(linha_atual) > 48 and linha_atual[48:53].strip() != '':
                            # Arquivo pode nao ter essas informacoes???posicao vazia significa max tap=0
                            self.Tap_Max[aux] = float(linha_atual[48:53].strip())
                        # defasagem do transformador defasador
                        if len(linha_atual) > 53 and linha_atual[53:58].strip() != '':
                            # Arquivo pode nao ter essas informacoes???posicao vazia significa defasagem=0
                            self.fase[aux] = float(linha_atual[53:58].strip())
                        # o numero da barra a ter a tensao controlado pelo trafo com tap
                        if len(linha_atual) > 58 and linha_atual[58:64].strip() != '':
                            # Arquivo pode nao ter essas informacoes?posicao vazia significa que nao tem barra control
                            self.Barra_Ctrl_tap[aux] = int(linha_atual[58:64].strip())
                        # capacidade normal da linha
                        if len(linha_atual) > 64 and linha_atual[64:68].strip() != '':
                            # Arquivo pode nao ter essas informacoes???posicao vazia significa CapLinhaNormal=0
                            self.Capacidade_Normal_Linha[aux] = float(linha_atual[64:68].strip())
                        # capacidade de emergencia da linha
                        if len(linha_atual) > 68 and linha_atual[68:72].strip() != '':
                            # Arquivo pode nao ter essas informacoes???posicao vazia significa CapLinhaEmer=0
                            self.Capacidade_Emergencia_Linha[aux] = float(linha_atual[68:72].strip())
                        # numero de taps
                        if len(linha_atual) > 72 and linha_atual[72:74].strip() != '':
                            # Arquivo pode nao ter essas informacoes???posicao vazia significa numtaps=0
                            self.Numero_de_taps[aux] = int(linha_atual[72:74].strip())
                        # ##Falta Cq?????????????
                        # Pula para a proxima linha
                        linha_atual = next(arquivo)
                        aux += 1

        # Transformacao dos valores de resistencia e reatancia em pu e calculo da impedancia (Z) e admitancai (Y)
        self.R_lin   = self.R_lin / 100  # sempre 100 pois valores lidos estao em porcentagem
        self.X_lin   = self.X_lin / 100  # sempre 100 pois valores lidos estao em porcentagem
        self.B_shunt = self.B_shunt / 2 / 100  
        self.Z_lin   = self.R_lin + 1j*self.X_lin

        # Separacao das linhas do sistema em seus tipos (1-linha de transmissao | 2-trafo em fase | 3-trafo defasador):
        for nlinha in range(self.contador_Linhas):

            # Linha de transmissao
            if self.tap[nlinha] == 0 and self.fase[nlinha] == 0:
                self.Tipo_Elemento[nlinha] = 0

            # Trafo em fase fixo
            elif self.tap[nlinha] != 0 and self.fase[nlinha] == 0:
                self.Tipo_Elemento[nlinha] = 2

            # Trafo em fase variavel
            elif self.tap[nlinha] != 0 and (self.Tap_Ma[nlinha] or self.Tap_Min[nlinha]) != 0:
                self.Tipo_Elemento[nlinha] = 1

            # Trafo defasador
            elif self.fase[nlinha] != 0:
                self.Tipo_Elemento[nlinha] = 3

            else:
                self.Tipo_Elemento[nlinha] = 4

        # Imprime dados lidos
        # print(self.BARRA_DE)
        # print(self.Abertura_Barra_De)
        # print(self.Operacao_Linha)
        # print(self.Abertura_Barra_Para)
        # print(self.BARRA_PARA)
        # # print(self.Circuito_Barra)
        # print(self.Estado_Linha)
        # print(self.Proprietario_Linha)
        # print(self.R_lin)
        # print(self.X_lin)
        # print(self.B_shunt)
        # print(self.tap)
        # print(self.Tap_Min)
        # print(self.Tap_Max)
        # print(self.fase)
        # print(self.Barra_Ctrl_tap)
        # print(self.Capacidade_Normal_Linha)
        # print(self.Capacidade_Emergencia_Linha)
        # print(self.Numero_de_taps)
        # print(self.Z_lin)
        # print(self.Admitancia_Linha)
        # print(self.Tipo_Elemento)
 
 
