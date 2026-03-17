# Implementação de Fatorial

Este repositório tem como objetivo mostrar 3 formas diferentes de versões de algoritmos para resolução de Fatorial

## Iterativo

Utiliza estruturas de repetição (for ou while) para multiplicar sequencialmente os números de 1 até n.
* Exemplo:
```python
  def fatorial(n):
    i = 0
    fat = 1
    while i < n:
        i+=1
        fat*=i
    return fat
```
ou

```python
    def fatorial(n: int) -> int:
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
```

 Vantagens: Geralmente mais eficiente em termos de memória e tempo de processamento, pois não cria múltiplas camadas na pilha de execução (stack)

 ## Recursivo
 
 A função resolve o fatorial dividindo o problema em casos menores, chamando a si mesma até atingir o caso base (1! = 1 ou 0! = 1)
 * Exemplo:
```python
   def fatorial_rec(n: int) -> int:
    if(n <= 1):
        return 1
    else:
        return n * fatorial_rec(n - 1)
```

Vantagens: Código mais conciso e próximo da definição matemática.
Desvantagens: Pode ser menos eficiente e consumir mais memória (stack overflow) se
for muito grande.
  
