real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 5.06
print('Com R${:.2f} você consegue comprar U$$ {:.2f}'.format(real, dolar))