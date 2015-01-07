#coding:utf-8
#vidade0 = 0
vidade1 = 0
nmenor = ""
nmaior = ""
tidade = 0

contador = input("Insira a quantidade de pessoas para cadastrar: ")
x = contador

nome = raw_input("Insira seu nome: ")
idade = input("Insira o sua idade: ")
tidade += idade
vidade0 = idade
nmenor = nome
if idade > vidade1:
	vidade1 = idade
	nmaior = nome

elif idade < vidade0:
	vidade0 = idade
	nmenor = nome	
contador -= 1 

while contador > 0:
	nome = raw_input("Insira seu nome: ")
	idade = input("Insira o sua idade: ")
	tidade += idade

	if idade > vidade1:
		vidade1 = idade
		nmaior = nome

	elif idade < vidade0:
		vidade0 = idade
		nmenor = nome		
	contador -= 1 

midade = tidade/x
print "Pessoa mais nova: %s com %i de idade."%(nmenor,vidade0)
print "Pessoa mais velha: %s com %i de idade."%(nmaior,vidade1)
print "A média das idades é %.2f."%(float(midade))