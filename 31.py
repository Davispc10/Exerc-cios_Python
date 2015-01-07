#coding:utf-8
sobra = 0
centena = 0
dezena = 0
unidade = 0

numero = int(input("Insira um valor menor que 1000: "))
if numero < 1000 and numero > 0:
	if numero > 99:
		centena = numero/100
		sobra = numero%100				
		if sobra > 0:
			dezena = sobra/10
			sobra = sobra%10			
			if sobra > 0:
				unidade = sobra

	elif numero > 9:		
		dezena = numero/10
		sobra = numero%10	
		if sobra > 0:
			unidade = sobra	

	elif numero > 0:
		unidade = numero
	

	if centena > 1:
		ncentena = "centenas"
	elif centena == 1:
		ncentena = "centena"
	if dezena > 1:
		ndezena = "dezenas"	
	elif dezena == 1:
		ndezena = "dezena"
	if unidade > 1:
		nunidade = "unidades"
	elif unidade == 1:
		nunidade = "unidade"

else:
	print "Valor inválido"
if centena > 0 and dezena > 0 and unidade > 0:
	print "%i: %i %s, %i %s e %i %s."%(numero,centena,ncentena,dezena,ndezena,unidade,nunidade)
else:
	if centena > 0 and dezena > 0:
		print "%i: %i %s e %i %s."%(numero,centena,ncentena,dezena,ndezena) 
	else:
		if centena > 0 and unidade > 0:
			print "%i: %i %s e %i %s."%(numero,centena,ncentena,unidade,nunidade)
		else:
			if dezena > 0 and unidade > 0:
				print "%i: %i %s e %i %s."%(numero,dezena,ndezena,unidade,nunidade)
			else:
				if centena > 0:
					print "%i: %i %s."%(numero,centena,ncentena)
				else:
					if dezena > 0:
						print "%i: %i %s."%(numero,dezena,ndezena)
					else:	
						if unidade > 0:
							print "%i: %i %s."%(numero,unidade,nunidade)
