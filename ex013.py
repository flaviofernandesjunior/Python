salário = float(input('Quanto é o salário do funcionário? R$ '))
novo = salário + (salário * 15 / 100)
print('O salário do funcionário era de R${:.2f} e com o aumento de 15% passou a ser R${:.2f}'.format(salário, novo))