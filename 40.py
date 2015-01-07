#coding:utf-8
contador = 3
homem = 0
mulher = 0
nhomem = ""
nmulher = ""

while(contador > 0):
	nome = raw_input("Insira um nome: ")
	sexo = raw_input("Insira o sexo(m/f): ")
	if sexo == 'm':
		homem += 1
	if sexo == 'f':
		mulher += 1
	contador -= 1

if homem == 1:
	nhomem = "homem"
else:
	nhomem = "homens"
if mulher == 1:
	nmulher = "mulher"
else:
	nmulher = "mulheres"

print "Existem %i %s e %i %s..."%(homem,nhomem,mulher,nmulher)
