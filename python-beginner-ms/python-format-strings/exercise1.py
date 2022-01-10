'''
#step 2
first_string = 'A literal string'
second_string = "A literal string"
print (second_string == first_string)

#step 3
#Quando quiser printar o ' (aspas), use a string com " (aspas duplas) e vice-versa
third_string = ' A single quoted literal string with a " double quote'
fourth_string = "A double quoted literal string with a ' single quote"
print(third_string)
print(fourth_string)

#step 4
#Você pode ser teimoso e usar um print com aspas simples e dentro aspas simples se usar o \ antes
fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string = "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with  a \n new line character'
eight_string = 'A literal string with a \t tab character'

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eight_string)

#step 5
#use o r na frente da string para printar tudo dentro das aspas raw
ninth_string = r"A literal string with a \n new line character printed raw"

print(ninth_string)


#step 6

tenth_string = A literal string
on more than one line
sometimes known as a verbatim string

eleventh_string = """Another literal string
    on more than one line
using double quotes"""

print(tenth_string)
print(eleventh_string)
'''
#step7

first = 'Conrad'
second = 'Grant'
third = 'Bob'
print(first, second)
print(first, second, third)
print(first, second, third, sep='-')
print(first, second, third, sep='-', end='.')
