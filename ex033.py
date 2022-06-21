a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b < a or b < c:
    menor = b
if c < a or c < b:
    menor = c
maior = a
if b > a or b > c:
    maior = b
if c > a or c > b:
    maior = c
print('O menor valor digitado foi o número {}'.format(menor))
print('O maior valor digitado foi o número {}'.format(maior))