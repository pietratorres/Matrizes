x = [2, 4, 6, 7, 10, 11, 14, 17, 20]
y = [4, 5, 6, 5, 8, 8, 6, 9, 12]

import matplotlib.pyplot as plt
plt.scatter(x, y)
#plt.show()

# Método dos Mínimos Quadrados
# Para fazer esse método manualmente vou primeiro criar todos termos da equação de a e b a partir das variáveis x e y. 
xquadrado = []
for dado in x:
    xquadrado.append(dado**2)

xvezesy = []
for posicao in range(0, len(x)):
    xvezesy.append(x[posicao]*y[posicao])
print(xvezesy)

# Somatórios 

somax = sum(x)
print(somax)

somay = sum(y)
print(somay)

somaxquadrado = sum(xquadrado)
print(somaxquadrado)
        
somax_AOquadrado = somax**2
print(somax_AOquadrado)

somaxvezesy = sum(xvezesy)
print(somaxvezesy)

#Cálculo A e B; onde an e bn = numerador da equação e ad e bd = denominador da equação
n = len(x) 

bn = (somaxquadrado*somay) - (somaxvezesy*somax) 
bd = (n*somaxquadrado) - somax_AOquadrado
b = bn/bd
print(b)

an = (n*somaxvezesy)-(somax*somay)
ad = (n*somaxquadrado)-(somax_AOquadrado)
a = an/ad
print(a)

# Calculo do novo y ajustado para minha reta (y = ax + b)
novoY= []
for dado in x:
    novoY.append(a*dado + b)
print(novoY)

plt.plot(x, novoY, label = 'y = 0.3678 x + 3.2807 ')
plt.legend(loc='upper right')
plt.show()