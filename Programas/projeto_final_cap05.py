'''
O projeto final tem por objetivo mostrar um código mais limpo e otmizado...
Foi construído com a tutoria de IA... que AUXILIOU mas primeiro eu desenvolvia e testava para depois melhorar.
'''
# Calculadora
print(f'*****Bem vindo a calculadora*****')
print(f'Selecione o número da operação desejada:\n 1-Soma\n 2-Subtração\n 3-Multiplicação\n 4-Divisão')
# primeira escolha para tratamento da entrada...
while (escolha := input('Digite a sua opção (1/2/3/4): ')) not in {'1', '2', '3', '4'}: # cria um loop para somente receber estas entradas
    print('Escolha uma opção válida!')

num1=float(input(f'Digite o primeiro número para a operação escolhida: '))

# faz tratamento para o caso de divisão por 0
while True:
    num2 = float(input('Digite o segundo número para a operação escolhida: '))
    if escolha == '4' and num2 == 0:
        print('Sabemos que não é possível dividir por zero! Escolha um valor válido.')
    else:
        break
 
# cria dicionário para otimizar a saída e o cálculo
operacoes = {
    '1': ('+', num1 + num2),
    '2': ('-', num1 - num2),
    '3': ('*', num1 * num2),
    '4': ('/', num1 / num2)
}

# Recuperando o operador e o resultado
operador, resultado = operacoes[escolha] # A chave (escolha) é usada para acessar o par (operador, resultado).

print(f'A conta escolhida foi: {num1} {operador} {num2} = {resultado}')






