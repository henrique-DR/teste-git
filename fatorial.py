# #Fatorial com *for*
# print('====== Fatorial ======')
# # def fatorial(n: int) -> int:
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     return res

#Fatorial com *while*
def fatorial(n):
    i = 0
    fat = 1
    while i < n:
        i+=1
        fat*=i
    return fat

n = int(input('Número para fatorar: '))
print(f'O fatorial de {n} é {fatorial(n)}')
