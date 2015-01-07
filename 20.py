#coding:utf-8
idade = input("Insira sua idade: ")

print "Classificação"
if idade > 4:
	if idade > 4 and idade < 8:
		print "Infantil A"
	else:
		if idade > 7 and idade < 11:
			print "Infantil B"
		else:
			if idade > 10 and idade < 14:
				print "Juvenil A"
			else:
				if idade > 13 and idade < 18:
					print "Juvenil B"
				else:
					if idade > 17:
						print "Adulto"
else:
	print "Voce é muito novo..."
