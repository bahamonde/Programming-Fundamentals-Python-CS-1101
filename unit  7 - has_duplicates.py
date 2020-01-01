# ---------------------- Variables and function of the book ---------------

alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

# From Section 11.2 of:

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press.

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d


#------------------------------------ PART 1 ------------------------

def has_duplicates(a):
    histogram(a)
    resp = histogram(a)
    r = resp.values()

    c = map(lambda x: x >= 2, r)  #Map to check items >=2
    g = list(c)  #Return a list of False or True

    if True in g:   #Check id any item of g is True, if it is, the function have duplicates letters
        return True
    else:return False



print("Part 1 - Have duplicate letters? ", has_duplicates("fdsaa"))




# ------------------------------- PART 2 -----------------------


def missing_letters(s):
    x = alphabet
    a = histogram(s)# using the function histogram()
    a=sorted(a)
    for i in a: # using sort to put in alphabetical order
        if i in alphabet: # check the letter is in alphabet
            x = x.replace(i,'')# delete the letter from alphabet
    return x


print("test 2.1 - The missing letters are: ", missing_letters("dy")) #To show the missing letters



for i in test_miss: # function test_miss
    if len( missing_letters(i) ) == 0:
        print(i, 'is using all letters')
    else:
        print("Test 2.2 - " ,i , 'is missing the letters: ', missing_letters(i))


#INSTRUCOES

"""
Comece com o seguinte código Python.

alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 


# Downey, A. (2015). Pense em Python: como pensar como um cientista da computação. Needham, Massachusetts: Green Tree Press.


def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 
     
Copie o código acima em seu programa, mas escreva você mesmo o outro código. Não copie nenhum código de outra fonte.

Parte 1

Escreva uma função chamada has_duplicates que use um parâmetro de string e retorne True se a string tiver caracteres repetidos. Caso contrário, ele deve retornar False.

Implemente has_duplicates criando um histograma usando a função histograma acima. Não use nenhuma das implementações de has_duplicates fornecidas no seu livro. Em vez disso, sua implementação deve usar as contagens no histograma para decidir se há duplicatas.

Escreva um loop sobre as strings na lista test_dups fornecida. Imprima cada sequência na lista e se possui ou não duplicatas com base no valor de retorno de has_duplicates para essa sequência. Por exemplo, a saída para "aaa" e "abc" seria a seguinte.

aaa tem duplicatas
abc não tem duplicatas

Imprima uma linha como uma das alternativas acima para cada uma das cadeias de caracteres em test_dups.

Parte 2

Escreva uma função chamada missing_letters que pega um parâmetro de string e retorna uma nova string com todas as letras do alfabeto que não estão na string de argumento. As letras na sequência retornada devem estar em ordem alfabética.

Sua implementação deve usar um histograma da função histograma. Também deve usar o alfabeto variável global. Ele deve usar essa variável global diretamente, não através de um argumento ou uma cópia local. Ele deve percorrer as letras do alfabeto para determinar quais estão faltando no parâmetro de entrada.

A função missing_letters deve combinar a lista de letras ausentes em uma string e retornar essa string.

Escreva um loop sobre as seqüências de caracteres na lista test_miss e chame missing_letters com cada string. Imprima uma linha para cada sequência listando as letras ausentes. Por exemplo, para a cadeia "aaa", a saída deve ser a seguinte.


aaa is missing letters bcdefghijklmnopqrstuvwxyz 

Se a string tiver todas as letras do alfabeto, a saída deve dizer que usa todas as letras. Por exemplo, a saída para o próprio alfabeto da string seria a seguinte.

abcdefghijklmnopqrstuvwxyz uses all the letters 

Imprima uma linha como uma das alternativas acima para cada uma das cadeias de caracteres em test_miss.

"""