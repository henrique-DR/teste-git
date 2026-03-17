# #Fatorial com *for* (iterativo)
# print('====== Fatorial ======')
# # def fatorial(n: int) -> int:
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     return res

#Fatorial com *while* (iterativo)
def fatorial(n):
    i = 0
    fat = 1
    while i < n:
        i+=1
        fat*=i
    return fat


#Fatorial Recursivo
n = int(input('Número para fatorar: '))
print(f'O fatorial de {n} é {fatorial(n)}')



def fatorial_rec(n: int) -> int:
    if(n <= 1):
        return 1
    else:
        return n * fatorial_rec(n - 1)
