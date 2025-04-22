import numpy
#importando os arquivos que vou usar
A1 = numpy.loadtxt( r'C:\Users\pietr\Downloads\Data_and_code\Data and code\chap01_SVD\A1.dat')
b1 = numpy.loadtxt( r'C:\Users\pietr\Downloads\Data_and_code\Data and code\chap01_SVD\b1.dat')
DetA1 = numpy.linalg.det(A1)
print ('O determinante de A1 é:', DetA1)
postoA1 = postoA1 = numpy.linalg.matrix_rank(A1)
print ('O posto de A1 é:', postoA1)

#Calculando a matriz por SVD (U,S e V)
svdA1 = numpy.linalg.svd(A1)
#Criando as variáveis necessárias para calcular a pseudo-inversa
s_inv = numpy.diag(1/svdA1.S)
u_trans = svdA1.U.T
v = svdA1.Vh.T
b_trans = b1.reshape(-1,1)
#Calculando a pseudo-inversa
A1_pseudo_inv = v@s_inv@u_trans
#Calculando o X por SVD 
Xs_svd = A1_pseudo_inv@b_trans
#Visualizando o resultado 
print("Os valores de X por SVD são:", Xs_svd)
