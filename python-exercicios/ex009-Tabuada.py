# Forma 01
numero = int(input("Digite um número e veja a Tabuada a seguir: \n"))
print("-"*20)
print("Tabuada do número {} :".format(numero))
print("-"*20)
# Criar um For:
for contador in range(1,11):
    print("{} x {:2} = {}".format(numero,contador,(numero*contador)))
