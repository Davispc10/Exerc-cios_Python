#coding:utf-8
import os
x = 0
receita = 0

while(x != 4):
	print "1 - Depósito"
	print "2 - Retirada"
	print "3 - Saldo"
	print "4 - Sair do algoritmo"
	x = input()
	if x == 1:
		valordeposito = input("Insira o valor do depósito: ")
		receita += valordeposito	
		os.system("clear")
	if x == 2:
		valorretirada = input("Insira o valor da retirada: ")
		receita -= valorretirada
		os.system("clear")
	if x == 3:
		print "Seu saldo é:",receita


print "ByeBye..."