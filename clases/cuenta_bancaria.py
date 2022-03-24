import random
saldo1 = random.randint(0,10000)
print("El saldo de la primera cuenta bancaria es: ", saldo1)
saldo2 = random.randint(0,10000)
print("El saldo de la segunda cuenta bancaria es: ", saldo2)
num_movimientos_max = 5 
class cuenta_bancaria:
    def __init__(self, ID, nombre, fechaA, saldo, numero):
        self.ID=ID
        self.nombre=nombre
        self.fechaA=fechaA
        self.saldo=saldo
        self.numero=numero  
       
    def cuenta_Bancaria1(retirar,ingresar,transferir):
        print("Cuenta bancaria 1. Seleccione: ")
        print(" 1.retirar")
        print(" 2.transferir")
        print(" 3.ingresar")
        print()
        eleccion = int(input("Cuál es tu elección?: "))

        if eleccion == 1:
            retirar =int(input("¿Cuánto dinero quieres retirar?:"))
            while retirar != num_movimientos_max:
                if retirar > saldo1:
                    print("No puedes retirar dinero")
                else:
                    print("Ha retirado su dinero correctamente, tu saldo actual es: ", )
                    print(saldo1-retirar)
                break  
        elif eleccion == 2:
            transferir =int(input("¿Cuánto dinero quieres transferir?:"))
            while transferir != num_movimientos_max:
                if transferir > saldo1:
                    
                    print("No puedes transferir dinero")
                else:
                    print("Ha transferido su dinero correctamente, tu saldo actual es ")
                    print("Primera cuenta bancaria: ")
                    print(saldo1-transferir)
                    print("Tu saldo actual es ")
                    print("Segunda cuenta bancaria: ")
                    print(saldo2+transferir)
                break
        elif eleccion == 3:
            ingresar =int(input("¿Cuánto dinero quieres ingresar?:"))
            print("Tu saldo actual es: ")
            print(saldo1+ingresar)
    def cuenta_Bancaria2(retirar,ingresar,transferir):
        print("Cuenta bancaria 2. Seleccione: ")
        print(" 1.retirar")
        print(" 2.transferir")
        print(" 3.ingresar")
        print()
        eleccion = int(input("Cuál es tu elección?: "))

        if eleccion == 1:
            retirar =int(input("¿Cuánto dinero quieres retirar?:"))
            while retirar != num_movimientos_max:
                if retirar > saldo2:
                    print("No puedes retirar dinero")
                else:
                    print("Ha retirado su dinero correctamente, tu saldo actual es: ", )
                    print(saldo2-retirar)
                break  
        elif eleccion == 2:
            transferir =int(input("¿Cuánto dinero quieres transferir?:"))
            while transferir != num_movimientos_max:
                if transferir > saldo2:
                    print("No puedes transferir dinero")
                else:
                    print("Ha transferido su dinero correctamente, tu saldo actual es ")
                    print("Segunda cuenta bancaria: ")
                    print(saldo2-transferir)
                    print("Tu saldo actual es ")
                    print("Primera cuenta bancaria: ")
                    print(saldo1+transferir)
                break
        elif eleccion == 3:
            ingresar =int(input("¿Cuánto dinero quieres ingresar?:"))
            print("Tu saldo actual es: ")
            print(saldo2+ingresar)
print(cuenta_bancaria.cuenta_Bancaria1("retirar","transferir", "ingresar"))
print(cuenta_bancaria.cuenta_Bancaria2("retirar","transferir", "ingresar"))



