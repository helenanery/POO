import Pizza

if __name__ == "__main__":
    pizza = Pizza()  

    
    print("Digite o sabor da pizza: ")
    pizza.set_sabor(input())  

    
    print("Digite quanto tempo de preparo: ")
    pizza.set_tempo(int(input()))  

    pizza.print_pizza()