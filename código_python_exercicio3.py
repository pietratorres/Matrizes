#para importar a biblioteca que eu vou usar
import numpy as np
#para criar as duas variáveis
A = np.asarray([[4,-1,0,-1,0,0],[0,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,0,0,-1,4,-1],[0,0,-1,0,-1,4]])
B = np.asarray([30,20,60,30,20,60])
#para inverter a matriz A
A_inv = np.linalg.inv(A)
#para visualizar minha matriz A
print(A_inv)
#para transpor a matriz B em forma escalar
B_trans = B.reshape(-1,1)
#para visualizar minha matriz transposta
print(B_trans)
#para visualizar minha matriz inversa
print(A_inv)
#para calcular o produto entre matrizes
ans = A_inv.dot(B_trans)
#para visualizar as respostas
print('As temperaturas nos pontos 1,2,3,4,5,6 respectivamente são:', ans)