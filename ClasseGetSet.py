class mesada:
    def __init__(self, mesada=0):
        self.mesada = mesada

    def get_mesada(self):
        return self._mesada

    def set_mesada(self, x):
        self._mesada = x


var = mesada()
var.set_mesada(150.00)
print(var.get_mesada())

print(var._mesada)
