# n = int(input('Digite um número: '))
# ('Digte um número!')
# print(n + 1)
try:
    n = int(input('Digite um número: '))
    print(n + 1)
except ValueError: 
    print('Tem que ser um número!')