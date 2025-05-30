# ======= arquivo: loja/produto.py =======
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco *= (1 - percentual/100)

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"
