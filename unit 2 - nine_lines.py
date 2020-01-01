#Define the new_line function to print 1 line
def new_line():

    print('.')

#Define the three_lines function that is using the new_line function to print 3 lines
def three_lines():

    new_line()

    new_line()

    new_line()



#Define the nine_lines function that is using the three_lines function to print 9 lines

def nine_lines():

    three_lines()

    three_lines()

    three_lines()




#Define the clear_screen function that is using all functions before to print 25 lines
def clear_screen():
    nine_lines()
    nine_lines()

    three_lines()
    three_lines()

    new_line()


#Call the nine_lines function and print . 9 times
print(nine_lines())

#print empty line to separate the functions
print('')

#Call the last function clear_screen and print . 25 times
print(clear_screen())



#INSTRUCOES
"""
Escreva uma função neste arquivo chamada nine_lines que use a função three_lines (fornecida abaixo) para imprimir um total de nove linhas.

Agora adicione uma função denominada clear_screen que use uma combinação das funções nine_lines, three_lines e new_line (fornecidas abaixo) para imprimir um total de vinte e cinco linhas. A última linha do seu programa deve chamar first nine_lines e depois a função clear_screen.

A função three_lines e new_line são definidas abaixo para que você possa ver as chamadas de funções aninhadas. Além disso, para facilitar visualmente a contagem das linhas "em branco", o comando de impressão dentro de new_line imprimirá um ponto no início da linha:


def new_line():

    print('.')

def three_lines():

    new_line()

    new_line()

    new_line()

É muito útil se você imprimir um espaço reservado entre a impressão de 9 linhas e a impressão de 25 linhas. Isso facilitará a leitura dos resultados para seus avaliadores. Um espaço reservado pode ser impresso como "Imprimindo nove linhas" ou "Chamando clearScreen ()"."""






