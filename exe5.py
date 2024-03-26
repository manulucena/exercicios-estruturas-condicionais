#exercício 6 da lista 1
n1 = int(input("Infome o primero número: "))
n2 = int(input("Infome o segundo número: "))
cod = int(input("Entre 1 e 4, informe o número do código: "))

if (cod==1):
    soma = n1+n2
    print(f"A soma é igual a {soma}")
elif (cod==2):
    subtracao = n1-n2
    print(f"A subtração é igual a {subtracao}")
elif (cod==3):
    multiplicacao = n1*n2
    print(f"A multiplicação é igual a {multiplicacao}")
elif (cod==4):
    if (n2!=0):
        divisao = n1/n2
        print(f"A divisão é igual a {divisao}")
    else:
        print("A divisão por zero não existe!")
else:
    print("Código inválido!")
