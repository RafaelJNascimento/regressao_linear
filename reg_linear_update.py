# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import matplotlib.pyplot as plt
import numpy as np

#Código original do Rafael para carregar o dataset 

def load(dataset):
  with open(dataset) as ds:
    d = []
    for l in ds.readlines():
      l = l.split()
      d.append([float(value) for value in l])
    return np.array(d)

def plot(x, y, b):
  # plota os pontos atuais   
  # s = np.abs(y) esse valor pode ser útil para personalizar o Scatter Plot no futuro 

  plt.scatter(x, y, c = x, cmap='viridis',  marker = "o", s = 10)
  plt.plot(x, b, color='red')
  
  plt.axvline(0, c=(.5, .5, .5), ls = '--')
  plt.axhline(0, c=(.5, .5, .5), ls = '--')
  
  plt.colorbar()

  #legenda e título do gráfico
  plt.title('Modelos de regressão Linear')
  plt.xlabel('velocidade do vento – m/s')
  plt.ylabel('variável de saída: potência gerada – kWatts')
  plt.savefig('img/update.jpg')
  plt.show()
  
  

def main():
  base = load('aerogerador.dat')
  # separa as colunas do vetor
  x, y = base[:,0], base[:,1]
  n = len(y)

  # valor de beta_1 e beta_0
  beta_1 =  (np.sum([x[i]*y[i] for i in range(0, len(x))]) - (1/n) * np.sum(y) * np.sum(x)) / (np.sum(x**2) - (1/n) * np.sum(x)**2)

  beta_0 = np.mean(y) - beta_1 * np.mean(x)

  # cria a equacao da reta
  y_chap = beta_0 + beta_1 * x


  print('Beta 1: {}\nBeta 0: {}\n'.format(beta_1, beta_0))
  print('\n')

  plot(x,y,y_chap)


if __name__ == "__main__":
  main() 


# %%



