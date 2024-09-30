import Pedido
import PropriedadeRural

if __name__ == "__main__":
    pedido1 = Pedido(30, 3)
    pedido1.retorna_valores()

    print("----------------------------------------------------------------------------------------------")

    propriedade_rural = PropriedadeRural("Campos", 2000, "Eduardo")
    propriedade_rural.retorna_valores1()
