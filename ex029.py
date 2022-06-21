velocidade = float(input('Qual a velocidade atual do veículo? '))
if velocidade > 80:
    print('MULTADO!! Você ultrapassou o limite de velocidade')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa no valor de {:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')
