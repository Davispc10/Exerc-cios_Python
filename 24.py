#coding:utf-8

ano = int(input("Insira um ano de 4 alarismos: "))

if ano % 400 == 0:
	bissexto = 1
if ano % 4 == 0 and ano % 100 != 0:
	bissexto = 1
else:
	bissexto = 0
if bissexto == 1:
	print "O ano %i é bissexto"%ano
else:
	print "O ano %i não é bissexto"%ano