#Fatorial
print('====== Fatorial ======')
def fatorial(n: int) -> int:
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# n = int(input('Digite um número: '))
# ('Digte um número!')
# print(n + 1)
try:
    n = int(input('Digite um número: '))
    print(fatorial(n))
except ValueError: 
    print('Tem que ser um número!')
