import random
numrand = random.randint(1, 100)
numutil = int(input("Escolhe um num: "))
while numutil != numrand:
    if numutil < numrand:
        print("O número é maior.")
    else:
        print("O número é menor.")
    numutil = int(input("Tenta novamente: "))
print("Acertou!")