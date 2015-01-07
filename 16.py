#coding:utf-8

valor = input("Insira um valor: ")
valor = int(valor)
n100 = valor/100
sobra = valor%100
n50 = sobra/50
sobra = sobra%50
n20 = sobra/20
sobra = sobra%20
n10 = sobra/10
sobra = sobra%10
n5 = sobra/5
sobra = sobra%5
n2 = sobra/2
sobra = sobra%2
n1 = sobra/1

print "Voce inseriu o valor: %i"%valor
print "Quantidades de notas:"
print "100 reais:",n100
print "50 reais:",n50
print "20 reais:",n20
print "10 reais:",n10
print "5 reais:",n5
print "2 reais:",n2
print "Moedas:",n1