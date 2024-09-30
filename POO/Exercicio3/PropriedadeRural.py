class PropriedadeRural:
    def __init__(self, nome, area, proprietario):
        self.nome = nome
        self.area = area
        self.proprietario = proprietario

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def get_proprietario(self):
        return self.proprietario

    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    def plantar(self):
        print("Plantando na " + self.nome + " do " + self.proprietario)

    def adubar(self):
        print("Adubando a " + self.nome)

