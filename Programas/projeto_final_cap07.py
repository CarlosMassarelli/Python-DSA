'''
Projeto de criação de um jogo como prova final do capítulo 7 do curso
Desenvolvimento do jogo da forca, onde o usuário deve adivinhar uma palavra
'''
import os
import requests
import re
import random
from bs4 import BeautifulSoup

def limpa_tela():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass

# Desenho da forca em cada etapa de erro
forca_desenho = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]

def obter_palavra_aleatoria():
    try:
        url = 'https://pt.wikipedia.org/wiki/Hist%C3%B3ria'
        headers = {'User-Agent': 'Mozilla/5.0'}
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        texto = sopa.get_text()
        palavras = re.findall(r'\b[A-ZÀ-ÿa-zà-ÿ]{5,}\b', texto)
        palavras_filtradas = [p for p in palavras if p.isalpha() and not p.isupper()]
        if palavras_filtradas:
            return random.choice(palavras_filtradas).upper()
        else:
            raise ValueError("Nenhuma palavra adequada encontrada.")
    except Exception as e:
        print("Erro ao buscar palavra da Wikipedia:", e)
        return "PYTHON"

def jogo_da_forca(palavra):
    palavra = palavra.upper()
    letras_descobertas = ['_' for _ in palavra]
    letras_erradas = []
    tentativas = 0

    while tentativas < 6 and '_' in letras_descobertas:
        try:
            limpa_tela()
            print(forca_desenho[tentativas])
            print("Palavra:", ' '.join(letras_descobertas))
            print("Letras erradas:", ', '.join(letras_erradas))

            tentativa = input("Informe uma letra: ").strip().upper()

            if not tentativa.isalpha() or len(tentativa) != 1:
                print("Digite apenas uma letra.")
                input("Pressione ENTER para continuar...")
                continue

            if tentativa in letras_descobertas or tentativa in letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
                input("Pressione ENTER para continuar...")
                continue

            if tentativa in palavra:
                for i, letra in enumerate(palavra):
                    if letra == tentativa:
                        letras_descobertas[i] = tentativa
            else:
                letras_erradas.append(tentativa)
                tentativas += 1
        except OSError as e:
            print("Erro de sistema durante o jogo:", e)
            break

    try:
        limpa_tela()
        print(forca_desenho[tentativas])
        if '_' not in letras_descobertas:
            print("Parabéns! Você adivinhou a palavra:", palavra)
        else:
            print("Você perdeu! A palavra era:", palavra)
    except Exception as e:
        print("Erro ao finalizar o jogo:", e)

# Executar com palavra aleatória da Wikipedia:
jogo_da_forca(obter_palavra_aleatoria())
