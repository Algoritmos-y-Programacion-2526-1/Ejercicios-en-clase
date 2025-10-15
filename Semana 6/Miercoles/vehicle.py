class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__saldo = 0

    def get_nombre(self):
        return self.__nombre
    
    def set_saldo(self, valor, operacion):
        if operacion == "+":
            if valor > 10000:
                print("ERROR")
            else:
                self.__saldo += valor
        elif operacion == "-":
            if self.__saldo - valor < 0:
                print("ERROR!!")
            else:
                self.__saldo -= valor
        else:
            print("ERROR!!")

    def get_saldo(self):
        return self.__saldo
