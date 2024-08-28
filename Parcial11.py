class vehiculos:
    def __init__(self, color, velocidad, marcha, modelo):
        self.color=color
        self.velocidad=velocidad
        self.marcha=marcha
        self.modelo=modelo
        
moto= vehiculos("negro","0","150km/h","honda")
carro=vehiculos("azul","0","162km/h","ferrari")

print(type(moto))
print(type(carro))

print(moto.color, moto.velocidad, moto.marcha, moto.modelo)
print(carro.color, carro.velocidad, carro.marcha, carro.modelo)