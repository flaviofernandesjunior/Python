preço = float(input('Qual é o valor do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produto que custava RS{:.2f} com o desconto de 5% ficará custando apenas {:.2f}'.format(preço, novo))
