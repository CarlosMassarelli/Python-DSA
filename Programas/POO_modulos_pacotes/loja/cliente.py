# ======= arquivo: loja/cliente.py =======
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = []

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.append(produto)

    def total_compra(self):
        return sum(p.preco for p in self.carrinho)

    def __str__(self):
        return f"Cliente: {self.nome}, Itens no carrinho: {len(self.carrinho)}"
