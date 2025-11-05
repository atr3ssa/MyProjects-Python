#nome=input("Qual o seu nome?")
#print("Prazer em te conhecer {:<20}!".format(nome))
#print("Prazer em te conhecer {:>20}!".format(nome))
#print("Prazer em te conhecer {:=^20}!".format(nome))
#print("Prazer em te conhecer {:^20}!".format(nome))
n1= int(input("Digite um número: "))
n2= int(input("Digte outro número: "))
soma=n1+n2
subtracao=n1-n2
multi=n1*n2
div=n1/n2 
div_inteira=n1//n2
resto_div=n1%n2
potencia=n1**n2
print("A soma vale {}".format(soma), end=' ')
print("A subtração vale {}".format(subtracao), end=' ')
print("A Multiplicação vale {}".format(multi), end=' ')
print("A Divisão vale {:.3f}".format(div), end=' ') #ponto flutuante (Quantas casas antes da vírgula)
print("A Divisão Inteira vale {}".format(div_inteira))
print("O Resto da visão vale {}".format(resto_div))
print("A Potencialização vale {}".format(potencia))
