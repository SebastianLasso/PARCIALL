class Mascotas:
    def __init__(self, color, raza, edad, peso):
        self.color=color
        self.raza=raza
        self.edad=edad
        self.peso=peso
        
gato= Mascotas("blanco","angora","4","5kg")
loro=Mascotas("vede","guacamayo","6","450g")

print(type(gato))
print(type(loro))

print(gato.color, gato.raza, gato.edad, gato.peso)
print(loro.color, loro.raza, loro.edad, loro.peso)
