#coding:utf-8
import string

resposta = 'S'
bom = 0
ruim = 0

while resposta == 'S' or resposta == 'N':	
	resposta = raw_input("Voce gostou do produto?(S/N): ")
	resposta = resposta.upper()
	if resposta == 'S':
		bom += 1
	if resposta == 'N':
		ruim += 1
if bom > ruim:
	print "Bom"
elif bom < ruim:
	print "Ruim"
else:
	print "Empate                       