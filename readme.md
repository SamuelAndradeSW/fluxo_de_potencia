
# Fluxo de Potência Não-Linear do Sistema IEEE 14 Barras com análise de contingência "n-1".

O presente trabalho teve como objetivo o desenvolvimento de um algoritmo para o cálculo do Fluxo de Potência Não-Linear do Sistema IEEE 14 Barras com análise de contingência "(n-1)".
Foi utilizado o método de Newton-Raphson para a solução do sistema não-linear de equações. O algoritmo foi implementado em Python e os resultados obtidos foram satisfatórios. Foi possível verificar a estabilidade do sistema elétrico de potência estudado, mesmo em situações de contingência.
Portanto, o algoritmo desenvolvido neste trabalho pode ser considerado uma ferramenta
útil para o estudo de sistemas elétricos de potência, permitindo a realização de análises de contingência de forma precisa e eficiente.




## 1 - Introdução

O cálculo de fluxo de potência é uma ferramenta fundamental em sistemas de potência, com o objetivo de garantir a estabilidade e segurança do sistema. O fluxo de potência é determinado com base nas características dos elementos do sistema e nas condições de carga. Os cálculos podem ser lineares ou não lineares, sendo que os não lineares são aplicáveis a sistemas de potência mais complexos.
Nesse contexto, o método de Newton-Raphson é uma técnica iterativa amplamente utilizada
para resolver cálculos de fluxo de potência não lineares. Esse método é capaz de convergir rapidamente para uma solução precisa. Para implementar o método de Newton-Raphson, é necessário construir um modelo matemático do sistema de potência, incluindo as equações de fluxo de potência e de restrição. Essa implementação pode ser realizada utilizando uma linguagem de programação como o Python.
Este relatório apresentará os fundamentos teóricos do cálculo de fluxo de potência em
sistemas de potência, com ênfase nos cálculos não lineares e na implementação do método de Newton-Raphson em Python. A partir deste estudo, será possível entender a importância do cálculo de fluxo de potência para garantir a estabilidade e segurança do sistema de potência, além de apresentar uma implementação prática do método de Newton-Raphson em Python para solucionar cálculos de fluxo de potência não lineares.
## 2 - Proposta do trabalho

Este trabalho tem como objetivo principal desenvolver o cálculo de fluxo de potência não-
linear do sistema IEEE 14 Barras (figura 1), levando em consideração a análise de contingência "n-1". O critério de estabilidade "n-1"é uma importante ferramenta utilizada na avaliação da segurança e estabilidade dos sistemas elétricos de potência. O objetivo deste critério é garantir que, mesmo com a retirada de um dispositivo ou equipamento do sistema, o sistema possa continuar operando em condições ideais de operação.

No caso em estudo, as linhas de transmissão do sistema IEEE 14 Barras serão retiradas
(exceto as linhas de transmissão com LTC) para realizar a análise de contingência "n-1". Para isso, será desenvolvido o cálculo de fluxo de potência não-linear, levando em consideração as características não lineares dos elementos do sistema.

O desenvolvimento do cálculo de fluxo de potência não-linear será realizado utilizando o
método de Newton-Raphson, que é uma técnica iterativa amplamente utilizada para resolver
cálculos não lineares. A implementação do método de Newton-Raphson será realizada utilizando a linguagem de programação Python.

Ao final deste trabalho, espera-se ter desenvolvido o cálculo de fluxo de potência não-linear do sistema IEEE 14 Barras e ter realizado a análise de contingência "n-1", levando em consideração a retirada das linhas de transmissão do sistema. Além disso, espera-se ter implementado o método de Newton-Raphson em Python para resolver cálculos não lineares, o que poderá ser aplicado em outras análises de sistemas elétricos de potência.



![IEEE](https://github.com/SamuelAndradeSW/fluxo_de_potencia/blob/main/fluxo%20de%20potencia/data/IEEE%2014%20barras.png)


## 3 - Desenvolvimento

O cálculo do fluxo de potência não-linear é um problema matemático que envolve a solução de um sistema de equações não-lineares. Para um sistema elétrico de potência com n barramentos, as equações de fluxo de potência podem ser representadas por:

![equações](https://github.com/SamuelAndradeSW/fluxo_de_potencia/blob/main/fluxo%20de%20potencia/data/equa%C3%A7%C3%B5es%20de%20fluxo%20de%20pot%C3%AAncia.png)

onde Pi e Qi são as componentes ativas e reativas da potência na barra i, Vi é a magnitude da tensão na barra i, Gij e Bij são as partes real e imaginária da admitância entre as barras i e j, respectivamente, e θij é a diferença de fase entre as barras i e j.

A solução do sistema de equações não-lineares pode ser obtida por meio de métodos
numéricos, como o método de Newton-Raphson. O método de Newton-Raphson é um método
iterativo que busca a solução do sistema de equações a partir de um valor inicial. A cada iteração, o método calcula a matriz jacobiana do sistema de equações, que é uma matriz n × n cujos elementos são as derivadas parciais das equações em relação às variáveis do sistema. Em seguida, o método calcula a solução aproximada do sistema de equações por meio da seguinte equação:

![jacobiana](https://github.com/SamuelAndradeSW/fluxo_de_potencia/blob/main/fluxo%20de%20potencia/data/matriz%20jacobiana.png)

onde ∆θ e ∆V são os vetores de correção das variáveis de fase e magnitude, respectivamente, H, N, M e L são as submatrizes da jacobiana, rθ e rV são os vetores das equações não-lineares, representando as diferenças entre as potências ativas e reativas calculadas e as potências ativas e reativas medidas.


## 4 Resultados:

Para a implementação do Fluxo de Potência Não-Linear com o Método de Newton-Raphson
em Python, foram realizados testes no sistema IEEE 14 Barras com análise de contingência (n-1) em que foram retiradas as Linhas de Transmissão do Sistema (exceto as LT’s com LTC).

Os resultados obtidos mostraram uma convergência do método em um número satisfatório
de iterações, indicando que o algoritmo foi bem-sucedido em calcular o fluxo de potência no sistema elétrico em questão. Além disso, foi possível observar a mudança na distribuição de potência ativa e reativa em diferentes barras do sistema após a contingência (n-1) ser aplicada.

## 5 Conclusão

Diante do exposto, o presente trabalho teve como objetivo principal o desenvolvimento de
um algoritmo para o cálculo do Fluxo de Potência Não-Linear do Sistema IEEE 14 Barras com
análise de contingência "(n-1)"e, posteriormente, a apresentação dos resultados obtidos.

Foi possível verificar que o método de Newton-Raphson se mostrou eficiente para a solução
do sistema não-linear de equações, permitindo a obtenção de resultados precisos e confiáveis. Além disso, os resultados obtidos mostraram a estabilidade do sistema elétrico de potência estudado, mesmo em situações de contingência.

Portanto, conclui-se que o algoritmo desenvolvido neste trabalho pode ser considerado
uma ferramenta útil e importante para o estudo de sistemas elétricos de potência, permitindo a realização de análises de contingência de forma precisa e eficiente.


## Referência

Monticelli, Alcir José. Fluxo de carga em redes de energia elétrica. São Paulo: Editora
Blucher, 1983.
