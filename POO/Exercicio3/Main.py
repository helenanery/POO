import Pedido
import PropriedadeRural

if __name__ == "__main__":
    pedido = Pedido(30, 3)
    pedido.pagar()
    pedido.cancelar()

    print("------------------------------------")

    propriedade_rural = PropriedadeRural("Campos abertos", 20000, "Eduardo")
    propriedade_rural.adubar()
    propriedade_rural.plantar()
