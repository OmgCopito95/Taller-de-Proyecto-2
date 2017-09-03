from flask import Flask
from flask import render_template
from flask import request
import estacionMeteorologica

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST']) # Se requiere GET para poder cargar la pagina por primera vez


def index():
    frecuencia = action_form()
    estacionMeteorologica.generar_datos(frecuencia) 
    temp,hum,pa,viento = estacionMeteorologica.leer_datos()
    promedioTemp = calcular_promedio10(temp)
    promedioHum = calcular_promedio10(hum)
    promedioPa = calcular_promedio10(pa)
    promedioVient =  calcular_promedio10(viento)
    return render_template('index.html',frec = frecuencia,promTemp=promedioTemp,promHum=promedioHum,promPa=promedioPa,
        promV=promedioVient,ultTemp=temp[len(temp)-1] ,ultHum=hum[len(hum)-1] ,ultPa=pa[len(pa)-1] ,ultV=viento[len(viento)-1])

def action_form():
    if request.method == 'POST':
        data=request.form
        frecuencia=int(data["frec"])
        if frecuencia < 200: # Evita que se generen grandes cantidades de datos
            return frecuencia
        else:
            return 5
    else:
        return 5


def calcular_promedio10(lista):
    if len(lista) >= 10:
        suma = 0
        for i  in range(len(lista)):
            if i >= len(lista)-10:
                suma = suma + float(lista[i])
        return suma / 10
    else:
        return "XXX" #No hay sufiente valores para obtener el promedio


if __name__ == "__main__":
    app.run (host = '127.0.0.1', port = 5000)


