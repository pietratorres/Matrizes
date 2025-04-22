#importando a bibliotca que vou usar
import numpy
#importando os arquivos que vou usar
A = numpy.loadtxt( r'C:\Users\pietr\Downloads\Data_and_code\Data and code\chap01_SVD\A.dat' )
b = numpy.loadtxt( r'C:\Users\pietr\Downloads\Data_and_code\Data and code\chap01_SVD\b.dat' )
#visualizando se os arquivos estão corretos
print(A)
print(b)
#calculando a inversa de A
A_inv = numpy.linalg.inv(A)
print(A_inv)
b_trans = b.reshape(-1,1)
print(b_trans)
Xs = A_inv@b_trans
print('Os valores de X são:', Xs)
DetA = numpy.linalg.det(A)
print('O determinante de A é:', DetA)
postoA = numpy.linalg.matrix_rank(A)
print('O posto de A é:', postoA)
#Calculando as matrizes do SVD (U, S, V)
svdA = numpy.linalg.svd(A)
#Criando as variáveis necessárias para calcular a pseudo-inversa
s_inv = numpy.diag(1/svdA.S)
u_trans = svdA.U.T
v = svdA.Vh.T
#Calculando a pseudo-inversa
A_pseudo_inv = v@s_inv@u_trans
#Calculando o X por SVD 
Xs_svd = A_pseudo_inv@b_trans
#Visualizando o resultado 
print("Os valores de X por SVD são:", Xs_svd)