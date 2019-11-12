class Perro:
    def __init__(self, nombre,apellidos, sexo , edad, raza, color,dueño):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo=sexo
        self.edad=edad
        self.raza=raza
        self.color=color
        self.dueño=dueño
        
    def traes_el_omnitrix (self):
        print("La informacion del canino es: ")
        print("Nombre: "+self.nombre)
        print("Apellidos : "+self.apellidos)
        print("Sexo: "+self.sexo)
        print("Edad: "+self.edad)
        print("Raza: "+self.raza)
        print("Color del pelaje : "+self.color)    
        print("Es propiedad de : "+self.dueño)
        print("")  
        
        
nombre = input("Nombre del perro aqui: ")        
apellidos = input("Apellidos del perro: ")
sexo = input("Sexo del perro: ")
edad = input("Edad del perro: ")
raza= input("Raza del perro: ")
color=input("Color del perro: ")
dueño=input("Su dueño es: ")
print("")

perro = Perro(nombre,apellidos,sexo,edad,raza,color,dueño)
perro.traes_el_omnitrix()