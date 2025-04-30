# Para fazer a média vou somar os dados e dividir pela quantidade de dados 
dados = [0.90, 1.42, 1.30, 1.55, 1.63, 1.32, 1.35, 1.47, 1.95, 1.66, 1.96, 1.47, 1.92, 1.35, 1.05, 1.85, 1.74, 1.65, 1.78, 1.71, 2.29, 1.82, 2.06, 2.14, 1.27]
soma = sum(dados)
print(soma)
n = len(dados)
print('Existem', n, 'dados no conjunto')
media = soma/n
print('A média dos dados é:', media)

# Para fazer a mediana vou ordenar os dados, descorbrir a posição da mediana através da quantidade de dados dividido por dois e encontrar o valor correspondente a posição da mediana. Em caso da mediana ser impar vamos somar os dois valores e dividir por dois. 
dados_ordenados = sorted(dados)
print(dados_ordenados)
posicao_da_mediana = n/2
print('A posição da mediana é', posicao_da_mediana)
dado_1_mediana = dados_ordenados[11]
print('O elemento de posição 12 é', dado_1_mediana)
dado_2_mediana = dados_ordenados[12]
print('O elemento de posição 13 é', dado_2_mediana)
mediana = (dado_1_mediana+dado_2_mediana) / 2 
print('A mediana é', mediana)

# Para fazer a moda vou fazer um looping que vai percorrer todo o conjunto de dados e contar o número de vezes que cada elemento aparece. 
contagem = {}
for elemento in dados:
    if elemento in contagem:
        contagem[elemento] += 1
    else:
        contagem[elemento] = 1

contagem_maxima = 0
moda = []
for chave, valor in contagem.items():
    if valor > contagem_maxima:
        contagem_maxima = valor
        moda = [chave]
    elif valor==contagem_maxima:
        moda.append(chave)
print("A moda é:", moda)

# Para o cálculo do desvio padrão vou calcular todos termos da equação de dp separadamente. São eles: Cada elemento menos a média, Quadrado deste novo elemento, Somatório dos elementos, Somatório dos elementos dividido pelo número de elementos do conjunto de dados. 
elemento_menos_media = [elemento - media for elemento in dados]
print(elemento_menos_media)
quadrado_novo_elemento = [elemento **2 for elemento in elemento_menos_media]
print(quadrado_novo_elemento)
somatorio_elementos = sum(quadrado_novo_elemento)
print(somatorio_elementos)
somatorio_dividido_n = somatorio_elementos / n 
print(somatorio_dividido_n)
desv_pad = somatorio_dividido_n ** 0.5
print('O desvio padrão é:', desv_pad)

# Para o calculo de coeficiente de variação vou pegar o valor de desvio padrão e dividir pela média, ambos já calculados anteriormente.  
coef_varia = desv_pad/media
print('O coeficiente de variação é:', coef_varia)