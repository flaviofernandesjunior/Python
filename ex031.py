distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a iniciar uma viagem de {} km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Sua passagem custará R$ {:.2f}'.format(preço))