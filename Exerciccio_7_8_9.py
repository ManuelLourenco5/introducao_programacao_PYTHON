#Ler e validar o peso do utilizador
while True:
    try:
        peso = float(input("Indique o seu peso (kg): "))
        if peso <= 0:
            print("Por favor, insira um valor positivo para o peso.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Insira um número.")

#Ler e validar a altura do utilizador
while True:
    try:
        altura = float(input("Indique a sua altura (em metros ou cm): "))
        if altura <= 0:
            print("Por favor, insira um valor positivo para a altura.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Insira um número.")

#Converter a altura para metros, se estiver em centímetros
if altura > 2.50:
    alturaM = altura / 100
else:
    alturaM = altura

#Calcular o IMC
imc = peso / (alturaM ** 2)

#Determinar a categoria do IMC
if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Excesso de peso"
else:
    categoria = "Obesidade"

#Mostrar o resultado final formatado
print(f"O seu IMC é {imc:.2f} ({categoria})")
