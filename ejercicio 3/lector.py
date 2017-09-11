import time

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

if __name__ == "__main__":
    leer_datos()
