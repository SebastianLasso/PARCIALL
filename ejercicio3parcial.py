class Frutas:
    def __init__(self, color, sabor, tamaño, peso):
        self.color=color
        self.sabor=sabor
        self.tamaño=tamaño
        self.peso=peso
        
sandia= Frutas("rojo","dulce","grande","10kg")
piña=Frutas("amarillo","acido","pequeña","2kg")

print(type(sandia))
print(type(piña))

print(sandia.color, sandia.sabor, sandia.tamaño, sandia.peso)
print(piña.color, piña.sabor, piña.tamaño, piña.peso)