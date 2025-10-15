from vehicle import Persona

def x():
    persona = Persona("Antonio")
    persona.set_saldo(1000,"+")
    print(persona.get_saldo())
    persona.set_saldo(500,"-")
    print(persona.get_saldo())

x()