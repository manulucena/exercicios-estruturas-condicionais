h = float (input("Infoeme a sua altura: "))
sexo = str (input("Informe o seu sexo: "))

if (sexo == "masculino"):
    peso_ideal_homem = (72.7*h)-58
    print(f"O seu peso ideal é {peso_ideal_homem:.1f}kg")
else:
    peso_ideal_mulher= (62.1*h)-44.7
    print(f"O seu peso ideal é {peso_ideal_mulher:.1f}kg")