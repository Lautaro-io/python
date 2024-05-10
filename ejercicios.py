#Generador de contraseñas
#Para hacer un generador de contraseñas, lo primero que tenemos que hacer es importar 2 bibiotecas , las cuales van a ser "Random " y " String" 
import random
import string
def generador_de_contraseñas():
    longitud = int(input("Ingrese la longitud que desee para su contraseña: "))
    char= string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(char) for contraseña in range(longitud))
    print( contraseña)

#--------------------------------------------------------------------------------------
#En este ejercicio vamos a hacer un juego de piedra, papel o tijera
def juego():
    opciones = ["Piedra","Papel","Tijera"]
    while True:
        opcionJugador = input("Ingrese su opción!(Debe ser piedra,papel o tijera): ").capitalize()
        if opcionJugador not in opciones:
            print("Ingrese una opción válida!")
            continue
        break
    opcionMaquina = random.choice(opciones)
    print(f"Haz elegido {opcionJugador}")
    print(f"Tu oponente ha elegido {opcionMaquina}")
    if opcionJugador == opcionMaquina:
        print("Haz empatado!")
    elif (opcionJugador == "Piedra" and opcionMaquina == "Tijera") or (opcionJugador == "Papel" and opcionMaquina == "Piedra") or (opcionJugador == "Tijera" and opcionMaquina == "Papel"):
        print("Felicidades!,Haz ganado!")
    else :
        print("Haz perdido! Vuelve a intentar!")
        return juego()

#----------------------------------------------------------------------------------------------------------------------------------------
#Hacer una funcion que tome un caracter como argumento e identifique si es vocal o no
def es_vocal():
    caracter = input("Ingrese un caracter: ")
    vocales =["a","e","i","o","u"]
    if caracter.lower() in vocales:
        print("Es vocal")
    else:
        print("No es vocal")

#Ahora hacer una funcion que determine cuantas vocales hay en una palabra}
def cuantas_vocales():
    vocales =["a","e","i","o","u"]
    palabra = input("Ingrese una palabra: ")
    contador = 0 
    for char in palabra:
        if char in vocales:
            contador+=1
    print(contador)

#-------------------------------------------------------------------------------
class Cuenta:
    
    def __init__(self,titular,saldo) :
        self.titular = titular
        self.saldo = saldo

    def depositar(self,cantidad):
        self.saldo += cantidad
        print("Se depositaron: ",cantidad )

    def retirar (self,cantidad):
        self.saldo -= cantidad
        print("Se retiraron:" , cantidad)

    def mostrar (self):
        print(self.__dict__)

#------------------------------------------------------------------------------------------
#Hacer una funcion que tome la distancia y la velocidad y te calcule el tiempo que tardara en llegar a destino
def trayecto():
    distancia = int(input("Ingrese la distacia que quiere recorrer: "))
    velocidad = int(input("Ahora ingrese la velocidad promedio con la que va a manejar: "))
    tiempo = distancia / velocidad
    print(f"A una velocidad de {velocidad}km/hr, recorrer {distancia}km te tomaria {tiempo}horas")

#-------------------------------------------------------------------------------------------------
#crear una clase persona con los atributos nombre y edad  y mostrar los datos en consola
class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(self.__dict___)

    def esMayor(self, edad):
        if edad >= 18:
            print("Es mayor")


#--------------------------------------------------------------------------------
def sueldo():
    cantidadDeHoras = float(input("Ingrese la cantidad de horas que usted trabajó: "))
    hora = 3000
    salario = cantidadDeHoras * 3000
    print(salario)
#----------------------------------------------------------------------------------
def masaTotal():
    altura = float(input("Ingrese su altura: "))
    peso = float(input("Ingrese su peso: "))
    indiceDeMasa = peso / altura
    print(f"Su indice de masa corporal es de {round(indiceDeMasa,1)}")


