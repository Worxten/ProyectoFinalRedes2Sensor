from flask import Flask, render_template
import pyfirmata2
import os
delay = 0.5
ledRojo = 4;
ledAmarillo = 3;
ledAzul = 2;
estado = 0

puerto = pyfirmata2.Arduino.AUTODETECT
print(puerto)
tarjeta = pyfirmata2.Arduino(puerto)
tarjeta.samplingOn(100)
tarjeta.analog[0].enable_reporting()

def prenderRojo():
    tarjeta.digital[ledRojo].write(1)
    tarjeta.digital[ledAzul].write(0)
    tarjeta.digital[ledAmarillo].write(0)
def prenderAmarillo():
    tarjeta.digital[ledRojo].write(0)
    tarjeta.digital[ledAzul].write(0)
    tarjeta.digital[ledAmarillo].write(1)
def prenderAzul():
    tarjeta.digital[ledRojo].write(0)
    tarjeta.digital[ledAzul].write(1)
    tarjeta.digital[ledAmarillo].write(0)
def getEstado(valor):
    est=0
    if(valor<120):
        prenderAzul()
    if(valor>120 and valor<160):
        prenderAmarillo()
    if(valor>160):
        prenderRojo()
    return est

app = Flask(__name__)

@app.route('/')
def home():
    tarjeta.pass_time(delay)
    valorSensor = int(tarjeta.analog[0].read() * 1000)
    estado = getEstado(valorSensor)
    return render_template('home.html',valor=valorSensor)
def main():
    if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0', port=6699)
main()