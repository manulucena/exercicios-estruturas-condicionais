tipo = int(input("Informe o tipo de investimento, sendo 1 poupança e 2 fundos de renda fixa: "))
valor_investimento = float(input("Informe o valor investido: R$"))

if(tipo==1):
    rendimento_poupanca = valor_investimento + (valor_investimento*3/100)
    print(f"O valor corrigido da poupança após 1 mês será de R${rendimento_poupanca:.2f}")
elif(tipo==2):
    rendimento_fundos_renda_fixa = valor_investimento + (valor_investimento*4/100)
    print(f"O valor corrigido dos fundos de renda fixa após 1 mês será de R${rendimento_fundos_renda_fixa:.2f}")
else:
    print("Opção inválida!")
