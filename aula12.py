nome = str(input("Qual é o seu nome? "))
if nome == 'Flavio':
    print('Que nome bonito!')
elif nome == 'Carlos' or 'Igor' or 'Fernandinho':
    print('Que nome comum!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!' .format(nome))
