from random import randint
from os import remove
import time

def generar_datos(frecuencia):
	# Se generaran 20 valores random de Temperatura, Humedad, PA, Vel Viento.
	borrar_datos()
	for i in range(0,frecuencia):
		time.sleep(1)
		temp = randint (0,50)
		hum = randint (0,100) # porcentaje
		pa = randint(800,1500) # hPa
		viento = randint (0,200) # km/h
		with open("datos.txt", "a") as file:
			file.write("{0}/{1}/{2}/{3}\n".format(temp,hum,pa,viento))


def leer_datos():
	# lee los datos del archivo de texto
	temp = []
	hum = []
	pa = []
	viento = []

	with open("datos.txt", "r") as file:
		lineas = file.readlines()
		for l in lineas:
			datos = l.split("/")
			temp.append(datos[0]) 
			hum.append(datos[1])
			pa.append(datos[2])
			viento.append(datos[3][:-1]) #el -1 elimina el /n
	return temp,hum,pa,viento		
    

def borrar_datos():
	remove("datos.txt")
