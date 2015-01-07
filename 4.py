#coding:utf-8
pesoh = 0
pesom = 0

altura = input("Insira sua altura: ")
sexo = raw_input("Insira seu sexo(m/f): ")
peso = input("Insira seu peso: ")
if sexo == 'm':
	pesoh = (72.7*altura) - 58
	print "Seu peso ideal é",pesoh
	if(peso > pesoh):
		print "Voce está acima do peso"
	if(peso == pesoh):
		print "Voce está no peso certo"
	if(peso < pesoh):
		print "Voce está abaixo do peso"
else:
	pesom = (62.1*altura) - 44.7
	print "Seu peso ideal é",pesom
	if(peso > pesom):
		print "Voce está acima do peso"
	if(peso == pesom):
		print "Voce está no peso certo"
	if(peso < pesom):
		print "Voce está abaixo do peso"
