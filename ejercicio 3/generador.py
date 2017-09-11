import estacionMeteorologica
import time
from random import randint

def generar_datos():
    # Se generaran valores random de Temperatura, Humedad, PA, Vel Viento.
    # los escribe en un archivo de texto datos.txt
    # borrar_datos()
    frecuenciaGeneracion = 1 # [seg]
    while True:
        time.sleep(frecuenciaGeneracion)
        temp = randint (0,50)
        hum = randint (0,100) # porcentaje
        pa = randint(0,200) # hPa
        viento = randint (0,200) # km/h
        with open("datos.txt", "a") as file:
            file.write("{0}/{1}/{2}/{3}\n".format(temp,hum,pa,viento))

if __name__ == "__main__":
    generar_datos()
