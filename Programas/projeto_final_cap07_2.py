'''
Projeto de criação de um jogo como prova final do capítulo 7 do curso
Desenvolvimento do jogo da forca, onde o usuário deve adivinhar uma palavra
Esta versão aprimora o código original com melhorias na busca, validação de entrada e exibição do estado do jogo, além de separa a lógica do jogo em funções distintas.
'''
'''
Pseudocódigo do Jogo da Forca com palavra aleatória da Wikipédia

INICIAR programa

IMPORTAR módulos: os, requests, re, random, BeautifulSoup

FUNÇÃO limpa_tela():
    SE sistema for Windows:
        LIMPAR terminal com 'cls'
    SENÃO:
        LIMPAR terminal com 'clear'

LISTA forca_desenho com 7 desenhos da forca em diferentes estágios de erro

FUNÇÃO obter_palavra_aleatoria():
    TENTAR:
        ACESSAR página da Wikipédia sobre História
        COLETAR texto da página com BeautifulSoup
        EXTRAIR palavras com 5 ou mais letras (apenas letras, sem todas maiúsculas)
        ESCOLHER uma palavra aleatória da lista extraída
        RETORNAR palavra em maiúsculas
    SE erro ocorrer:
        IMPRIMIR mensagem de erro
        RETORNAR palavra padrão 'PYTHON'

FUNÇÃO jogo_da_forca(palavra):
    CONVERTER palavra para maiúsculas
    INICIALIZAR lista de letras_descobertas com "_" para cada letra
    INICIALIZAR lista de letras_erradas vazia
    INICIALIZAR contador de tentativas com 0

    ENQUANTO tentativas < 6 E ainda houver "_" em letras_descobertas:
        LIMPAR tela
        MOSTRAR estágio da forca de acordo com tentativas
        MOSTRAR progresso da palavra com letras descobertas
        MOSTRAR letras erradas

        SOLICITAR letra do jogador (input)
        VALIDAR se é uma única letra do alfabeto
            SE inválido: mostrar aviso e pedir novamente

        VERIFICAR se letra já foi tentada
            SE sim: mostrar aviso e pedir nova letra

        SE letra estiver na palavra:
            PERCORRER cada letra da palavra:
                SE for igual à tentativa: atualizar letras_descobertas
        SENÃO:
            ADICIONAR letra à lista de letras_erradas
            INCREMENTAR tentativas

    LIMPAR tela
    MOSTRAR desenho final da forca
    SE palavra foi descoberta:
        PARABENIZAR jogador
    SENÃO:
        INFORMAR que perdeu e mostrar palavra correta

EXECUTAR jogo_da_forca com resultado de obter_palavra_aleatoria()

'''
import os
import requests
import re
import random
from bs4 import BeautifulSoup

# Desenho da forca em cada etapa de erro
FORCA_DESENHO = [
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

def limpa_tela():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except OSError:
        pass

def obter_palavra_aleatoria():
    try:
        url = r'https://pt.wikipedia.org/wiki/Hist%C3%B3ria'
        headers = {'User-Agent': 'Mozilla/5.0'}
        resposta = requests.get(url, headers=headers, timeout=5)
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

def mostrar_estado(tentativas, letras_descobertas, letras_erradas):
    limpa_tela()
    print(FORCA_DESENHO[tentativas])
    print("\nPalavra:", ' '.join(letras_descobertas))
    print("Letras erradas:", ', '.join(letras_erradas))
    print(f"Tentativas restantes: {6 - tentativas}\n")

def validar_entrada(letra, letras_descobertas, letras_erradas):
    if not letra.isalpha() or len(letra) != 1:
        return "Digite apenas uma letra."
    if letra in letras_descobertas or letra in letras_erradas:
        return "Você já tentou essa letra. Tente outra."
    return ""

def atualizar_descobertas(palavra, tentativa, letras_descobertas):
    for i, letra in enumerate(palavra):
        if letra == tentativa:
            letras_descobertas[i] = tentativa

def jogo_da_forca(palavra):
    palavra = palavra.upper()
    letras_descobertas = ['_' for _ in palavra]
    letras_erradas = []
    tentativas = 0

    while tentativas < 6 and '_' in letras_descobertas:
        mostrar_estado(tentativas, letras_descobertas, letras_erradas)
        tentativa = input("Informe uma letra: ").strip().upper()

        erro = validar_entrada(tentativa, letras_descobertas, letras_erradas)
        if erro:
            print(erro)
            input("Pressione ENTER para continuar...")
            continue

        if tentativa in palavra:
            atualizar_descobertas(palavra, tentativa, letras_descobertas)
        else:
            letras_erradas.append(tentativa)
            tentativas += 1

    mostrar_estado(tentativas, letras_descobertas, letras_erradas)
    if '_' not in letras_descobertas:
        print("Parabéns! Você adivinhou a palavra:", palavra)
    else:
        print("Você perdeu! A palavra era:", palavra)

# Bloco main para executar o jogo
if __name__ == "__main__":
    jogo_da_forca(obter_palavra_aleatoria())
    while True:
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente == 's':
            jogo_da_forca(obter_palavra_aleatoria())
        elif jogar_novamente == 'n':
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida. Por favor, digite 's' ou 'n'.")
# Fim do código
