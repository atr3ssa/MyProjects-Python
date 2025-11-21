dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos km rodados? "))
valor_dia = dias_alugados*60
valor_km = km_rodados*0.15
valor_pagar = valor_dia+valor_km
print("O total a pagar é de R${:.2f}".format(valor_pagar))