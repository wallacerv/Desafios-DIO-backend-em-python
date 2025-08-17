class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("plim plim")
    
    def parar(self):
        print("paraaaaaa")

    def correr(self):
        print("VRUMMMMMM")


b1 = bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
