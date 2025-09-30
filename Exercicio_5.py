nome=input("digite o seu nome:")
genero=input("digite o seu genero('f'ou'm')")
altura=int(input("digite a sua altura:"))

if genero=='m' or genero=='M':
    if altura>=(174):
        print("o",nome,"é alto")
    else:
        print("o",nome,"é baixo")


if genero=='f' or genero=='f':
    if altura>=(164):
        print("a",nome,"é alto")
    else:
        print("a",nome,"é baixo")