from flask import Flask
from flask import render_template
from flask import request
import lector

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET']) # Se requiere GET para poder cargar la pagina por primera vez


def index():
    frecuencia = action_form()
    temp,hum,pa,viento = lector.leer_datos()
    promedioTemp = calcular_promedio10(temp)
    promedioHum = calcular_promedio10(hum)
    promedioPa = calcular_promedio10(pa)
    promedioVient =  calcular_promedio10(viento)
    if temp:
        return render_template('index.html',frec = frecuencia,promTemp=promedioTemp,promHum=promedioHum,promPa=promedioPa,
            promV=promedioVient,ultTemp=temp[len(temp)-1] ,ultHum=hum[len(hum)-1] ,ultPa=pa[len(pa)-1] ,ultV=viento[len(viento)-1])
    else:
        return "No existen datos. Verifique que el sensor se encuentra conectado."

def action_form():
    # here we want to get the value of user (i.e. ?user=some-value)
    frecuencia = request.args.get('frec')
    if not frecuencia:
        return 15
    else:
        return frecuencia


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


