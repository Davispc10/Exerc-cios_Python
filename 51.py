#coding:utf-8
import time
import random
import os

quadrot = "-" * 70
quadrol = "-" * 70
ntartaruga = "T"
nlebre = "L"
passot = 0
passol = 0
posicaot = []
posicaol = []

while passol < 70 and passot < 70:
	os.system("clear")
	print "BANG!!!!"
	print "E ELES PARTIRAM!!!!"

	randomt = random.randrange(1,10)
	randoml = random.randrange(1,10)

	if randomt > 0 and randomt < 6:
		passot += 3
	if randomt > 5 and randomt < 8:
		passot -= 2
	if randomt > 7 and randomt < 11:
		passot += 1

	if randoml > 2 and randoml < 5:
		passol += 9
	if randoml > 4 and randoml < 6:
		passol -= 12
	if randoml > 5 and randoml < 9:
		passol += 1
	if randoml > 8 and randoml < 11:
		passol -= 2
	
	if passot < 0:
		passot = 0
	if passol < 0:
		passol = 0

	if passot == passol:
		posicaot = quadrot[:passot]+"OUCH!!!"+quadrot[:-passot-7]
		posicaol = quadrol[:passol]+"OUCH!!!"+quadrol[:-passol-7]
	else:
		posicaot = quadrot[:passot]+ntartaruga+quadrot[:-passot-1]
		posicaol = quadrol[:passol]+nlebre+quadrol[:-passol-1]

	# print passot
	# print passol
	print posicaot
	print posicaol

	time.sleep(0.5)
	
if passot >= 70:
	print "TARTARUGA VENCEU!!! YAY!!!"
elif passol >= 70:
	print "LEBRE VENCEU!!! YUCH!!!"
else:
	print "HOUVE UM EMPATE"
# elif passot >= 70 and passol >= 70:
# 	print "HOUVE UM EMPATE"
