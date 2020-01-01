# function to verificate if a number a is is divisible by number b

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


# calling a function 'is_divisible', i made another function to verificate if it is true the first time, and in another if i verificated if the result of the first math operation is divisible by b number. I used a nested conditional.

def is_power(x, y):
    if (is_divisible(x, y) == True):
        aBYb = x / y
        if (aBYb % y == 0):
            print(x, " is a power of ", y)
        else:
            print(x, " is not a power of ", y)
    else:
        print(x, " is not a power of ", y)


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))


#INSTRUCOES

"""
Faça o Exercício 6.4 do seu livro usando recursão e a função is_divisible da Seção 6.4. Seu programa pode assumir que ambos os argumentos para is_power são números inteiros positivos. Observe que o único número inteiro positivo que é uma potência de "1" é o próprio "1".

Após escrever sua função is_power, inclua os seguintes casos de teste em seu script para exercitar a função e imprimir os resultados:

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
"""