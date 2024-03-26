#exercício 5 da lista 2
horas_extras = int(input("Informe o número de horas extras do funcionário: "))
horas_faltas = int(input("Informe o número de horas faltas do funcionário: "))
hora_total = (horas_extras)-(2/3 * (horas_faltas))

if (hora_total>2400):
    print("A gratificação será de R$500,00.")
elif (hora_total>=1800 and hora_total<=2400):
    print("A gratificação será de R$400,00.")
elif (hora_total>=1200 and hora_total<=1800):
    print("A gratificação será de R$300,00.")
elif (hora_total>=600 and hora_total<=1200):
    print("A gratificação será de R$200,00.")
elif (hora_total<600):
    print("A gratificação será de R$100,00.")
