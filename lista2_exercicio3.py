import numpy as np

dados = np.array ([29.65, 28.55, 28.65, 30.15, 29.35, 29.75, 29.25, 30.65, 28.15, 29.85, 29.05, 30.25, 30.85, 28.75, 29.65, 30.45, 29.15, 30.45, 33.65, 29.35, 29.75, 31.25, 29.45, 30.15, 29.65, 30.55, 29.65, 29.25])
media = np.mean(dados)
dp = np.std(dados)
print('Média = ', media)
print('Desvio Padrão =', dp)

Intervalo = media-dp, media+dp
print('intervalo de valores', Intervalo)
