casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Vai pagar em quantos anos? '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de {:.2f}'.format(casa, anos, prestação))
if prestação <= minimo:
    print('Financiamento APROVADO')
else:
    print('Financiamento NEGADO')