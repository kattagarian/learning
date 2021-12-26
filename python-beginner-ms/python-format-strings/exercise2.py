'''
#step 2
#Faz a primeira letra ser maiúscula
message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())

#step 3
#Transforma todas as letras em minúsculas ou maiúsculas
message = 'hello world'
print(message.lower())
print(message.upper())

message = message.title()
print(message)
print(message.swapcase())

#step 4
#Diz quantas vezes um caractere apareceu na frase
location = 'Mississippi'
print(location.count('s'))
#retorna quantos caracteres há na string
print(len('how many characters in this string?'))

#step 5
#Verifica se uma string começa/termina com x caracteres
message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

#step 6
#Diz em que posição o caractere* está na string
message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))

#step 7
#Tira espaços da string
message = '    middle    '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')

#step 8
#Substitui uma string por outra
message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)
'''
#step 9
message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))