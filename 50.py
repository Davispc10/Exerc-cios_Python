#coding:utf-8
import random
valor = 101

resposta = random.randrange(0,100)
print resposta
while valor != resposta:
	valor = input("Insira um valor entre 0 e 100: ")
	if valor > resposta:
		print "Maior"
	elif valor < resposta:
		print "Menor"
	else:
		print "Acertoooooooooouuuuuuu..."