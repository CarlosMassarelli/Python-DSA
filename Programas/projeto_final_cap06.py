# Dividindo o arquivo em linhas e colunas

import os

BASE_DIR = os.path.dirname(__file__)  # Pega o caminho onde está o .py
file_path = os.path.join(BASE_DIR, 'arquivos', 'salarios.csv')

with open(file_path, 'r') as arq:
    data = arq.read()
    rows = data.split('\n')
    full_data = [row.split(',') for row in rows]
    print(full_data)

print('Número de linhas:', len(full_data))  # Imprime o número de linhas
print('Número de colunas:', len(full_data[0]))  # Imprime o número de colunas
print(f'\n')
print(f'usando o módulo csv para ler o arquivo {file_path}')
print(f'Organizando os dados em uma lista de listas')
print(f'Usando o delimitador "," e o caractere de citação como aspas duplas')
import csv

with open(file_path, newline='', encoding='utf-8') as arq: 
    leitor = csv.reader(arq, delimiter=',', quotechar='"')
    dados = list(leitor)
for linha in dados[:5]:  # Imprime as 5 primeiras linhas para conferência
    print(linha)

'''
# Outra forma de fazer o mesmo, mas com mais linhas de código

with open(r'e:/02-Cursos/22-Python/Python-DSA/Programas/arquivos/salarios.csv', 'r') as arq:
    data = arq.read()
    rows = data.split('\n')
    type(rows) # <class 'list'>
    full_data = []
    for row in rows: # iterando sobre as linhas
        columns = row.split(',') # separando as colunas
        full_data.append(columns) # adicionando as colunas à lista full_data
    print(full_data) 
'''