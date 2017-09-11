from flask import Flask
from flask import render_template
from flask import request
import lector
import time

app = Flask(__name__)

@app.route('/') # define la ruta con la que se ingresa en el explorador

# muestra la pagina

def index():
    frecuencia = 5 # frecuencia de muestreo
    temp,hum,pa,viento = lector.leer_datos()
    promedioTemp = calcular_promedio10(temp)
    promedioHum = calcular_promedio10(hum)
    promedioPa = calcular_promedio10(pa)
    promedioVient =  calcular_promedio10(viento)
    return render_template('index.html',frec = frecuencia,promTemp=promedioTemp,promHum=promedioHum,promPa=promedioPa,
        promV=promedioVient,ultTemp=temp[len(temp)-1] ,ultHum=hum[len(hum)-1] ,ultPa=pa[len(pa)-1] ,ultV=viento[len(viento)-1])

def calcular_promedio10(lista):
    if len(lista) >= 10:
        suma = 0
        for i  in range(len(lista)):
            if i >= len(lista)-10:
                suma = suma + float(lista[i])
        return suma / 10
    else:
        return "XXX" # No hay sufiente valores para obtener el promedio


if __name__ == "__main__":
    app.run (host = '127.0.0.1', port = 5000)
