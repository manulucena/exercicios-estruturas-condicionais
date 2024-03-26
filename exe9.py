#exercício 4 da lista 2
preco_do_produto = float (input("Informe o preço do produto: "))
codigo_de_origem = int (input("Informe o número do código de origem do produto: "))

if (codigo_de_origem == 1):
    print("O produto vem do Sul.")
elif (codigo_de_origem == 2):
    print("O produto vem do Norte.")
elif (codigo_de_origem == 3):
    print("O produto vem do Leste.")
elif (codigo_de_origem == 4):
    print("O produto vem do Oeste.")
elif (codigo_de_origem==5 or codigo_de_origem==6):
    print("O produto vem do Nordeste.")
elif (codigo_de_origem==7 or codigo_de_origem==8 or codigo_de_origem==9):
    print("O produto vem do Sudeste.")
elif (codigo_de_origem>=10 and codigo_de_origem<=20):
    print("O produto vem do Centro-Oeste.")
else:
    print("Origem do produto não especificada!")