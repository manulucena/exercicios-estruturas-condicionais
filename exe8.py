#exercício 3 da lista 2
idade = int (input("Informe a idade do nadador: "))

if (idade<5):
    print ("O nadador não está apto a entrar em nenhuma categoria")
elif (idade>=5 and idade<=7):
    print ("O nadador está apto a entrar na categoria infantil")
elif (idade>=8 and idade<=10):
    print ("O nadador está apto a entrar na categoria juvenil")
elif (idade>=11 and idade<=15):
    print ("O nadador está apto a entrar na categoria adolescente")
elif (idade>=16 and idade<=30):
    print ("O nadador está apto a entrar na categoria adulto")
else:
    print ("O nadador está apto a entrar na categoria sênior")
