class animal:
    def __init__(self, animal):
        self.animal=animal

    def Animal(pollo, gato, ornitorrinco):
        print("Seleccione: ")
        print("1. Pollo")
        print("2. Gato")
        print("3. Ornitorrinco")
        print()
        eleccion = int(input("Cuál es tu elección?: "))

        if eleccion == 1:
            print("Es un animal ovíparo")
        elif eleccion == 2:
            print("Es un animal mamífero")
        elif eleccion == 3:
            print("Es un animal ovíparo y mamífero")
print(animal.Animal("pollo", "gato", "ornitorrinco"))