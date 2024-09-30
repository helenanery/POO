class Pedido:
    def __init__(self, valor_total, numero_de_itens):
        self.valor_total = valor_total
        self.numero_de_itens = numero_de_itens

    def get_valor_total(self):
        return self.valor_total

    def set_valor_total(self, valor_total):
        self.valor_total = valor_total

    def get_numero_de_itens(self):
        return self.numero_de_itens

    def set_numero_de_itens(self, numero_de_itens):
        self.numero_de_itens = numero_de_itens

    def pagar(self):
        print("Pagando " + str(self.valor_total) + " do pedido")

    def cancelar(self):
        print("Cancelando pedido com " + str(self.numero_de_itens) + " itens")
