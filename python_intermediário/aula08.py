# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mutiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
        
print(mutiplicador(1,2,3,4,5))



def par_impar(numero):
    multiplo_dois = numero % 2 == 0
    
    if multiplo_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(1))
print(par_impar(2))
print(par_impar(3))
print(par_impar(4))