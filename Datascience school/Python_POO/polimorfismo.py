class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('ando caminando')
    
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('ando moviendome en mi bicicleta')

def main():
    persona = Persona('Ignacio')
    persona.avanza()

    ciclista = Ciclista('Daniela')
    ciclista.avanza()

if __name__ == '__main__':
    main()