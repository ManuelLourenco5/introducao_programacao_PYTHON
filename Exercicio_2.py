

#declara o valor do numero
numero=0
#inicia funçao true que enquanto for verdade adiciona 1
while True:
    numero+=1
    ##se o valor for 3 encerra a iteraçao e começa a proxima
    if numero ==3:
        continue
    ## se o valor for 5 encerra a iteraçao de vez
    if numero >5:
        break
    ## apresenta os valores
    print(numero)