palavras= ["leao", "animal", "jogar", "sim", "otorrinolaringologista"]

tam_maior_palavra=0
tam_menor_palavra=100

for palavra in palavras:
    if len(palavra)>tam_maior_palavra:
        tam_maior_palavra=len(palavra)
        maior_palavra=palavra

    if len(palavra)<tam_menor_palavra:
        tam_menor_palavra=len(palavra)
        menor_palavra=palavra
        
print("Lista de palavras:",palavras)
print("maior palavra:",maior_palavra,"letras",tam_maior_palavra)
print("menor palavra:",menor_palavra,"letras",tam_menor_palavra)