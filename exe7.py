#exercício 2 da lista 2
custo_de_fabrica = float (input("Informe o valor de custo de fábrica: "))

if (custo_de_fabrica<=12000.00):
    preco_consumidor_1= custo_de_fabrica + (custo_de_fabrica*5/100)
    print(f"O preço ao consumidor será de {preco_consumidor_1:.2f}")

elif (custo_de_fabrica>12000.00 and custo_de_fabrica<=25000.00):
    preco_consumidor_2 = custo_de_fabrica + (custo_de_fabrica*10/100) + (custo_de_fabrica*15/100)
    print(f"O preço ao consumidor será de {preco_consumidor_2:.2f}")

else:
    preco_consumidor_3 = custo_de_fabrica + (custo_de_fabrica*15/100) + (custo_de_fabrica*20/100)
    print(f"O preço ao consumidor será de {preco_consumidor_3:.2f}")