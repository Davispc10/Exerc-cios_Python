#coding:utf-8
qlata = 0.0
qgalao = 0.0
metrosq = input("Insira o numero de metros quadrados que desejar pintar: ")
litros = metrosq / 6.0
precol = 0
precog = 0
total1 = 0
total2 = 0
total3 = 0


if litros > 0:
	if litros >= 18.0:
		qlata = int(litros / 18.0)
		sobra = litros % 18.0		
		precol = qlata * 80
		if(sobra > 0.0):
			qlata += 1
			precol += 80
	else:
		if litros > 0.0:
			qlata += 1
			precol += 80
	total1 = precol

	print "Somente em latas"
	print "Quantidade de latas que precisará é: %i"%qlata
	print "Voce gastará um total de %.2f reais..."%total1

	if litros > 3.6:
		qgalao = int(litros / 3.6)
		sobra = litros % 3.6
		precog = qgalao * 25
		if(sobra > 0.0):
			qgalao += 1
			precog += 25
	else:
		if litros > 0.0:
			qgalao += 1
			precog += 25
	total2 = precog

	print "Somente em galoes"
	print "Quantidade de galões que precisará é: %i"%qgalao
	print "Voce gastará um total de %.2f reais..."%total2


	precog = 0
	precol = 0
	qgalao = 0
	qlata = 0
	if litros >= 18.0:		
		qlata = int(litros / 18.0)
		sobra = litros % 18.0		
		precol = qlata * 80
		if(sobra >= 3.6):	
			qgalao = int(sobra / 3.6)
			sobra = litros % 3.6	
			precog = qgalao * 25	
			if(sobra > 0.0):
				qgalao += 1
				precog += 25
		else:
			if(sobra > 0.0):
				qgalao += 1
				precog += 25
	else:
		if litros > 3.6:
			qgalao = int(litros / 3.6)
			sobra = litros % 3.6
			precog = qgalao * 25
			if(sobra > 0.0):		
				qgalao += 1
				precog += 25
		else: 
			qgalao = 1
			precog += 25
	total3 = precog + precol

	print "Com latas e galões"
	print "Quantidade de latas que precisará é: %i"%qlata
	print "Quantidade de galões que precisará é: %i"%qgalao
	print "Voce gastará um total de %.2f reais..."%total3
else:
	print"Voce não entrou com um valor válido"