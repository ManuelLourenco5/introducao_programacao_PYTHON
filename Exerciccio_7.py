peso = float(input("Indique o seu peso (kg): "))
altura = float(input("Indique a sua altura (em metros ou cm): "))

# Converter altura para metros, se necessário
if altura > 2.50:
    alturaM = altura / 100
else:
    alturaM = altura

# Calcular o IMC
imc = peso / (alturaM ** 2)

# Determinar a categoria
if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Excesso de peso"
else:
    categoria = "Obesidade"

# Mostrar resultado
print(f"O seu IMC é {imc:.2f} ({categoria})")
