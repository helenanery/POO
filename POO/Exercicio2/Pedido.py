class Pedido:
    def __init__(self, valor_total, numero_de_itens):
        self.valor_total = valor_total
        self.numero_de_itens = numero_de_itens

    def retorna_valores(self):
        print(self.valor_total)
        print(self.numero_de_itens)

