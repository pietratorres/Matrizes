#para importar a biblioteca que vou usar
import numpy
#para criar as variáveis 
S1 = numpy.asarray([[-6,2,0],[1,0,5],[2,3,3]])
S1X = numpy.asarray([[1,2,0],[3,0,5],[20,3,3]])
S1Y = numpy.asarray([[-6,1,0],[1,3,5],[2,20,3]])
S1Z = numpy.asarray([[-6,2,1],[1,0,3],[2,3,20]])
S2 = numpy.asarray([[1,1,1],[2,2,2],[0,1,2]])
S2X = numpy.asarray([[10,1,1],[20,2,2],[1,1,2]])
S2Y = numpy.asarray([[1,10,1],[2,20,2],[0,1,2]])
S2Z = numpy.asarray([[1,1,10],[2,2,20],[0,1,1]])

#para calcular o determinante das variáveis 
detS1 = numpy.linalg.det(S1)
detS1X = numpy.linalg.det(S1X)
detS1Y = numpy.linalg.det(S1Y)
detS1Z = numpy.linalg.det(S1Z)
detS2 = numpy.linalg.det(S2)
detS2X = numpy.linalg.det(S2X)
detS2Y = numpy.linalg.det(S2Y)
detS2Z = numpy.linalg.det(S2Z)

#para calcular X, Y e Z 
X1 = detS1X/detS1
Y1 = detS1Y/detS1
Z1 = detS1Z/detS1
X2 = detS2X/detS2
Y2 = detS2Y/detS2
Z2 = detS2Z/detS2

#para visualizar X, Y e Z
print ('O valor de X em S1 é:', X1)
print ('O valor de Y em S1 é:', Y1)
print ('O valor de Z em S1 é:', Z1)
print ('O valor de X em S2 é:', X2)
print ('O valor de Y em S2 é:', Y2)
print ('O valor de Z em S2 é:', Z2)

print ('O valor do determinante de S1 é:', detS1)
print ('O valor do determinante X de S1 é:', detS1X)
print ('O valor do determinante de S2 é:', detS2)
print ('O valor do determinante X de S2 é:', detS2X)
