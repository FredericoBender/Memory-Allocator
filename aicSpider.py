# -*- coding: utf-8 -*-
# Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
from math import pi

def padronizaMatriz(matriz):
  matriz = matriz.astype(float)
  matriz = matriz.transpose()
  for i in range(len(matriz)):
    maior = max(matriz[i])
    matriz[i] = [n/maior for n in matriz[i]]
  matriz = matriz.transpose()
  return matriz

def main(matrizGeral):
  # ------- PARTE 1: Criação do Fundo

  # Numero de categorias para plotar
  n = 4
  # Nome das variáveis
  #categorias=["Tempo Médio de Espera de Processos", "Número de Tentativas Falhas","Nível de Fragmentação da Memória","Tempo Médio para Alocação de Processos"]
  categorias=["TME", "NTF","NFM","TMA"]
  
  for i in range(len(matrizGeral)):
    del(matrizGeral[i][0])

  matrizGeral = np.array(matrizGeral)
  matrizGeral = padronizaMatriz(matrizGeral)
  # Valores que precisam ser definidos
  valoresFirst = matrizGeral[0]
  valoresBest =  matrizGeral[1]
  valoresWorst = matrizGeral[2]

  # Cálculo do ângulo de cada eixo baseado no número de variáveis
  angulos = [i / float(n) * 2 * pi for i in range(n)]
  angulos += angulos[:1]

  fig = plt.figure(figsize = (10, 5))


  # Inicializa o grafico (polar indica o grafico aranha)
  ax = fig.add_subplot(121, polar=True)

  # Para manter a primeira variável no topo
  ax.set_theta_offset(pi / 2)
  ax.set_theta_direction(-1)

  # Desenha um eixo por variável e adicional as labels
  plt.xticks(angulos[:-1], categorias)



  font = {'family' : 'Arial',
          'weight' : 'normal',
          'size'   : 13}

  plt.rc('font', **font)

  # ------- PART 2: Add plots

  # Significado de cada indice do vetor de dados
  # ["Tempo Médio de Espera de Processos", "Número de Tentativas Falhas","Nível de Fragmentação da Memória","Tempo Médio para Alocação de Processos"]

  # Curva First Fit
  valoresFirst = np.append(valoresFirst,valoresFirst[0])
  print(valoresFirst)
  ax.plot(angulos, valoresFirst, linewidth=2, linestyle='solid', label="First Fit")
  ax.fill(angulos, valoresFirst, 'b', alpha=0.1)

  # Curva Best Fit

  valoresBest = np.append(valoresBest,valoresBest[0])
  ax.plot(angulos, valoresBest, linewidth=2, linestyle='solid', label="Best Fit")
  ax.fill(angulos, valoresBest, 'r', alpha=0.1)

  # Curva Worst Fit

  valoresWorst = np.append(valoresWorst,valoresWorst[0])
  ax.plot(angulos, valoresWorst, linewidth=2, linestyle='solid', label="Worst Fit")
  ax.fill(angulos, valoresWorst, 'g', alpha=0.1)

  # Desenha os ylabels
  ax.set_rlabel_position(0)

  # Faz um vetor com 4 numeros para desenhar a indicação do eixo
  def defineY(valor):
    quarto = valor/4
    y = np.arange(0,valor+1,quarto)
    rounder = round(quarto)
    if (rounder == 0):
      rounder = 1
    y = [rounder*round(i/rounder) for i in y]
    return y
  # maiorValor = max([np.amax(valoresBest),np.amax(valoresWorst),np.amax(valoresFirst)])
  # y_ticks = defineY(maiorValor)
  y_ticks = [0.25,0.5,0.75,1]
  # Define os valores do eixo y
  plt.yticks(y_ticks, size=10)

  # Add legenda do plot
  plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))


  #Cria uma segunda figura para servir de espaço para legenda dos textos
  ax2 = fig.add_subplot(122,frameon=False)
  # Deixa figura sem eixos
  ax2.axes.get_xaxis().set_visible(False)
  ax2.axes.get_yaxis().set_visible(False)
  # inserir textos
  ax2.text(0, 0.35,u"NFM = Nível de Fragmentação da Memória")
  ax2.text(0, 0.45,u"NTF = Número de Tentativas Falhas")
  ax2.text(0, 0.55,u"TMA = Tempo Médio para Alocação de Processos")
  ax2.text(0, 0.65,u"TME = Tempo Médio de Espera de Processos")
  
  # Define nome da janela
  man = plt.get_current_fig_manager()
  man.canvas.set_window_title("Gráfico de análise dos resultados")
  
  #Posiciona janela no centro


  plt.show()