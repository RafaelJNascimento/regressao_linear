#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: Rafael J. Nascimento
# @email: rafaeljosev10@gmail.com
# license: MIT

import matplotlib.pyplot as plt
import numpy as np

def load(dataset):
  with open(dataset) as ds:
    d = []
    for l in ds.readlines():
      l = l.split()
      d.append([float(value) for value in l])
    return np.array(d)

def plot(x, y, b):
  # plota os pontos atuais 
  plt.scatter(x, y, color = "g", marker = "o", s = 30)

  # labels
  plt.title('Conjunto de dados do aerogerador')
  plt.xlabel('velocidade do vento – m/s')
  plt.ylabel('variável de saída: potência gerada – kWatts')
  plt.figure(2)

  # plota a linha de regressão 
  plt.plot(x, b, "--", color = "r") 
  
  # labels 
  plt.title('Modelos de regressão Linear')
  plt.xlabel('velocidade do vento – m/s')
  plt.ylabel('variável de saída: potência gerada – kWatts')
  plt.show()


def main():
  base = load('aerogerador.dat')
  # separa as colunas do vetor
  x, y = base[:,0], base[:,1]
  n = len(y)

  # valor de beta_1 e beta_0
  beta_1 =  np.sum(x*y) -(1/n) * np.sum(y)* np.sum(x)/ np.sum(n**2) - (1/n) * np.sum(x**2)
  beta_0 = np.mean(y) - beta_1 * np.mean(x)

  # cria a equacao da reta
  y_chap = beta_0 + beta_1 * x

  plot(x,y,y_chap)


if __name__ == "__main__":
  main()