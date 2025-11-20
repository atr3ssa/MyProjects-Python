preco_produto = float(input("Qual é o preço do produto? R$"))
desconto = preco_produto*5/100
preco_desconto =  preco_produto-desconto
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${}".format(preco_produto,preco_desconto))