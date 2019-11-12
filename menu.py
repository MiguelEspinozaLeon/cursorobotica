from persona import Persona

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
