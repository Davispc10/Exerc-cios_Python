# 1.Leia um valor de temperatura em graus Celsius e converta-o em graus Fahrenheit e Kelvin. A
# fórmula de conversão é:
# F = (9C + 160) / 5
# K = C + 273

#coding:utf-8

C = input("Insira um valor de temperatura em Celsius: ")
F = (9*C + 160) / 5
K = C + 273
print "O valor da temperatura em Fahrenheit e em Kelvin é: %.2f,%f" %(F,K)