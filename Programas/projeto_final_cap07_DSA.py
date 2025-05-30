'''
Construindo passo a passo pelo professor
'''
# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# import
import random
from os import system, name

# Função para limpar a tela
def limpa_tela():
    if name == 'nt':  # Windows
        _ = system('cls') #jogando para o _ para não gerar erro de retorno
    else:  # Linux ou Mac
        system('clear')
# Função
def game():
    limpa_tela()
    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta abaixo:\n")
    # Lista de palavras
    palavras = ["python", "programacao", "desenvolvimento", "computador", "tecnologia"]
    # Escolher uma palavra aleatória
    palavra = random.choice(palavras)
    # calcular o tamanho da palavra com list comprehension
    letras_descobertas = ['_' for letra in palavra]
    # número de tentativas
    chances = 6
    
    #lista para as letras erradas
    letras_erradas = []
    
    #Desenvolvendo a lógica do jogo
    while chances > 0:
        # print
        print(" ".join(letras_descobertas))
        print(f"Tentativas restantes: {chances}")
        print("Letras erradas:", " ".join(letras_erradas))
        # Entrada do usuário
        tentativa = input(f"\nDigite uma letra: ").lower()
        
        # Verificar se a letra já foi tentada
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
            else:
                chances -= 1
                letras_erradas.append(tentativa)
        # Verificar se a palavra foi descoberta
        if '_' not in letras_descobertas:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break
    # Verificar se o usuário perdeu                    
    if "_" in letras_descobertas:
        print("Você perdeu! A palavra era:", palavra)

# Bloco main para executar o jogo
if __name__ == "__main__":
    game()