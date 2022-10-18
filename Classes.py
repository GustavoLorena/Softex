class TV():
    def __init__(self, marca, tipo, polegadas):
        self.marca = marca
        self.tipo = tipo
        self.polegadas = polegadas


TV1 = TV("AOC", "LCD", "43")

TV2 = TV("Samsung", "OLED", "60")

TV3 = TV("LG", "LED", "32")

print(TV1.tipo, TV1.marca)

print(TV2.marca, TV2.polegadas)

print(TV3.polegadas, TV3.tipo)
