import random
saldo = random.randint(0,10000)
print("Tu saldo es: ", saldo)
num_movimientos_max = 5 
class cuenta_bancaria:
    def __init__(self, ID, nombre, fechaA, saldo, numero):
        self.ID=ID
        self.nombre=nombre
        self.fechaA=fechaA
        self.saldo=saldo
        self.numero=numero

    def cuenta_Bancaria(retirar,ingresar,transferir):
        print("Seleccione: ")
        print(" 1.retirar")
        print(" 2.transferir")
        print(" 3.ingresar")
        print()
        eleccion = int(input("Cuál es tu elección?: "))

        if eleccion == 1:
            print(retirar)
        elif eleccion == 2:
            print(transferir)
        elif eleccion == 3:
            print(ingresar)
        
    def Retirar(retirar): 
        retirar =int(input("¿Cuánto dinero quieres retirar?:"))
        while retirar != num_movimientos_max:
            if retirar > saldo:
                print("No puedes retirar dinero")
            else:
                print("Ha retirado su dinero correctamente, tu saldo actual es: ", )
                print(saldo-retirar)
            break      
        
    def Transferir(transferir):  
        transferir =int(input("¿Cuánto dinero quieres transferir?:"))
        while transferir != num_movimientos_max:
            if transferir > saldo:
                print("No puedes transferir dinero")
            else:
                print("Ha transferido su dinero correctamente")
            break
print(cuenta_bancaria.cuenta_Bancaria("retirar","transferir", "ingresar"))
print(cuenta_bancaria.Retirar("retirar"))
print(cuenta_bancaria.Transferir("transferir"))