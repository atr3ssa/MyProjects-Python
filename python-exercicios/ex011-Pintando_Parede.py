largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura*altura
litros_de_tinta = area/2
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede você precisará de {}L de tinta.".format(largura,altura,area,litros_de_tinta))