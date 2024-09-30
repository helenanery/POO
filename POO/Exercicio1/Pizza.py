
class Pizza:
    def __init__(self):
        self._sabor = ""
        self._tempo = 0

    # Getters
    def get_sabor(self):
        return self._sabor

    def get_tempo(self):
        return self._tempo

    # Setters
    def set_sabor(self, sabor):
        self._sabor = sabor

    def set_tempo(self, tempo):
        self._tempo = tempo

    # Método para imprimir informações da pizza
    def print_pizza(self):
        print("Sabor: " + self._sabor)
        print("Tempo de preparo: " + str(self._tempo) + " Minutos")
