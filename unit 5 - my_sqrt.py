import math               #In the part 2 of the exercise we need import the math library

# --------------------------------Building the my_sqrt() function ------------------------

def my_sqrt(a):           #start the my_sqrt() function with a parameter
    x = 2                 #start a x variable that receive 2 as value
    while True:           #Start a loop using while structure encapsulated inside the function
        y = (x + a / x) / 2       #iniciate the Newton's method logic of the algorithm
        if y == x:                #condition
            break
        x = y
    return(x)                     #return the variable x that received the y value




# --------------------------------Building the diff() function ----------------------------

def diff(a):               #start the diff() function with a parameter
    r = abs(my_sqrt(a) - math.sqrt(a))      #Using the abs math library's method to return the absolute value of its parameters
    return (r)             #return the variable r that received the abs method value





# --------------------------------Building the test_sqrt() function -------------------------

def test_sqrt():        #start the test_sqrt() function without parameter
    i = 1               #Start the variable i that received 1 as a value
    while i < 26:       #Start a loop using while structure that will repeat it 25 times
        #Asking to print messages and concatenate with i variable, my_sqrt function and the math library's sqrt method
        print('a = ', i, ' | my_sqrt(a) = ', my_sqrt(i), ' | math.sqrt(a) = ', math.sqrt(i), ' | diff = ', diff(i))
        i += 1          #i variable increment



print(test_sqrt())   #print the test_sqrt() function result


#INSTRUCOES

"""
Parte 1

Encapsule o seguinte código Python da Seção 7.5 em uma função chamada my_sqrt que usa a como parâmetro, escolhe um valor inicial para x e retorna uma estimativa da raiz quadrada de a.

while True:
     y = (x + a/x) / 2.0
     if y == x:
          break
     x = y 

Parte 2

Escreva uma função chamada test_sqrt que imprima uma tabela como a seguinte usando um loop while, em que "diff" é o valor absoluto da diferença entre my_sqrt (a) e math.sqrt (a).

a = 1 | my_sqrt (a) = 1 | math.sqrt (a) = 1.0 | diff = 0.0
a = 2 | my_sqrt (a) = 1.41421356237 | math.sqrt (a) = 1.41421356237 | diff = 2.22044604925e-16
a = 3 | my_sqrt (a) = 1,73205080757 | math.sqrt (a) = 1,73205080757 | diff = 0.0
a = 4 | my_sqrt (a) = 2.0 | math.sqrt (a) = 2.0 | diff = 0.0
a = 5 | my_sqrt (a) = 2.2360679775 | math.sqrt (a) = 2.2360679775 | diff = 0.0
a = 6 | my_sqrt (a) = 2.44948974278 | math.sqrt (a) = 2.44948974278 | diff = 0.0
a = 7 | my_sqrt (a) = 2.64575131106 | math.sqrt (a) = 2.64575131106 | diff = 0.0
a = 8 | my_sqrt (a) = 2.82842712475 | math.sqrt (a) = 2.82842712475 | diff = 4.4408920985e-16
a = 9 | my_sqrt (a) = 3.0 | math.sqrt (a) = 3.0 | diff = 0.0

Modifique seu programa para que ele produza linhas para valores de 1 a 25 em vez de apenas 1 a 9.
"""