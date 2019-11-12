class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, altura, color_ojos, color_cabello):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.altura = altura
        self.color_ojos = color_ojos
        self.color_cabello = color_cabello
        
    def mostrar_info(self):
        print("La informacion de la persona es: ")
        print("Nombre: "+self.nombre)
        print("Apellidos: "+self.apellidos)
        print("Sexo: "+self.sexo)
        print("Edad: "+self.edad)
        print("Altura: "+self.altura)
        print("Color de ojos: "+self.color_ojos)
        print("Color de cabello: "+self.color_cabello)
        print("")
        
    def volver_al_futuro(self):       
        print("Tu edad en 10 años es: ",(int(self.edad) +10))
        print("")
        
#inputs
"""
nombre= input("Ingrese nombre aqui: ")
apellidos = input("Ingrese apellidos aqui: ")
sexo = input("Ingrese sexo aqui: ")
edad = input("Ingrese edad aqui: ")
altura = input("Ingrese altura aqui: ")
color_ojos = input("Ingrese color de ojos aqui: ")
color_cabello = input("Ingrese color de cabello aqui: ")
print("")


persona = Persona(nombre,apellidos,sexo,edad,altura,color_ojos,color_cabello)
persona.mostrar_info()
"""

#ejecucion x
#pepito= Persona("La Rosalia", "Espinoza Robles", "Hombre", "21", "1.78", "azules Y verdes", "Negro")
#pepito.mostrar_info()
#pepito.volver_al_futuro()
