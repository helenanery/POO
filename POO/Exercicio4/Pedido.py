class Pedido:
    def __init__(self):
        self.itens = []  
        self.total = 0.0  
        self.quantidade_itens = 0  

    def adicionarItem(self, item):
        self.itens.append(item)  
        self.total += item.valor  
        self.quantidade_itens += 1  

    def imprimirPedido(self):
        print(f"Pedido contém {self.quantidade_itens} item(ns)")
        for i, item in enumerate(self.itens, start=1):
            print(f"Item {i}: {item.nome}, Valor: R$ {item.valor:.2f}")
        print(f"Total do pedido: R$ {self.total:.2f}")