from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['POST', 'GET']) # Se requiere GET para poder cargar la pagina por primera vez


def index():
    frecuencia = action_form()
    temp,hum,pa,viento = leer_datos()
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
    app.run (host='localhost', port=80)


