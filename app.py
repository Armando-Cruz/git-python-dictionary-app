from diccionario import getDefinition

print('-----------------------------------------------------------')
print('\t\t\t\t\tDiccionario Español')
print('-----------------------------------------------------------')


word = input('Buscar palabra: ')
definition = ''
try:
	definition = getDefinition(word)
except Exception as error:
	definition = error

print(f'\nResultado\n{definition}')