import Pedido
import Produto

if __name__ == "__main__":

    pedido = Pedido()

    produto1 = Produto("Notebook", 3500.00)
    produto2 = Produto("Mouse", 50.00)

    pedido.adicionarItem(produto1)
    pedido.adicionarItem(produto2)

    pedido.imprimirPedido()