'''
Aqui está um exemplo completo de um projeto orientado a objetos com múltiplos módulos em Python. Ele representa uma pequena loja com produtos e clientes, organizados em arquivos distintos, conforme boas práticas de modularização. 
'''
# ======= arquivo: main.py =======
from loja.cliente import Cliente
from loja.produto import Produto

def main():
    # Criando produtos
    p1 = Produto("Camisa", 100.0)
    p2 = Produto("Calça", 150.0)
    p2.aplicar_desconto(10)  # 10% de desconto

    # Criando cliente
    cliente = Cliente("Lucas")
    cliente.adicionar_ao_carrinho(p1)
    cliente.adicionar_ao_carrinho(p2)

    print(cliente)
    for item in cliente.carrinho:
        print(item)
    print(f"Total da compra: R${cliente.total_compra():.2f}")

if __name__ == "__main__":
    main()