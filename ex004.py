a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só espaço? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum()) #Letras e números
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas?' , a.islower())
print('Está capitalizada? ', a.istitle()) #Com apenas uma letra maiúscula