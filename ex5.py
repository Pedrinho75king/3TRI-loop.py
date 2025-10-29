usuarios = ["Capitão_Hunter", " ", " ", "Robert", "Adolfo", "Jefferson"]

for usuario in usuarios:
    if not usuario:
        continue

    for letra in usuario:
        if letra == "_":
            print(f"Ignorando '{usuario}' (vazio ou apenas espaços)")
            break

        if letra.islower():
            print(f"Ignorando '{usuario}' (contém letra minúscula)")
            break
else:
    print(f"Cadastrando usuário: {usuario}")