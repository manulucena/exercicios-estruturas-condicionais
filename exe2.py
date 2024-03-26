valor_venda = float(input("Informe o valor da venda: R$"))

if (valor_venda>=20.00):
    quantidade_cupons = valor_venda/20
    print(f"O cliente tem direito a {quantidade_cupons:.0f} cupons")
else:
    print("O cliente não tem direito aos cupons")
