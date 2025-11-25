def ler_peso():
    """
    Solicita ao utilizador que insira o seu peso em kg e valida a entrada.
    
    Retorna:
        float: O peso válido do utilizador em quilogramas.
    """
    while True:
        try:
            peso = float(input("Indique o seu peso (kg): "))
            if peso <= 0:
                print("Por favor, insira um valor positivo para o peso.")
                continue
            return peso
        except ValueError:
            print("Entrada inválida. Insira um número.")

def ler_altura():
    """
    Solicita ao utilizador que insira a sua altura e valida a entrada.
    Aceita altura em metros ou centímetros.

    Retorna:
        float: A altura do utilizador em metros.
    """
    while True:
        try:
            altura = float(input("Indique a sua altura (em metros ou cm): "))
            if altura <= 0:
                print("Por favor, insira um valor positivo para a altura.")
                continue
            # Converter para metros, se estiver em centímetros
            if altura > 2.50:
                altura = altura / 100
            return altura
        except ValueError:
            print("Entrada inválida. Insira um número.")

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura.
    
    Args:
        peso (float): Peso em quilogramas.
        altura (float): Altura em metros.

    Returns:
        float: O valor do IMC.
    """
    return peso / (altura ** 2)

def categorizar_imc(imc):
    """
    Determina a categoria do IMC de acordo com a classificação padrão.
    
    Args:
        imc (float): Valor do IMC.

    Returns:
        str: Categoria do IMC ("Abaixo do peso", "Peso normal", "Excesso de peso", "Obesidade").
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"

# --- Programa principal ---
peso = ler_peso()
altura = ler_altura()
imc = calcular_imc(peso, altura)
categoria = categorizar_imc(imc)

print(f"O seu IMC é {imc:.2f} ({categoria})")
