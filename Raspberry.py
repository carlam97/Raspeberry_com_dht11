# Programa : Sensor de temperatura DHT11 com Raspberry Pi
# Autor : 
 
# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import urllib.request

#Configurar API ThingSpeak
# APIJay 
myAPI  = '9JZPVTXX3VML3BPC'
#BaseURL
baseURL = "https://api.thingspeak.com/update?api_key="  + myAPI
#Teste da URL
##print(baseURL)
#Envio
#temp  = 25
#umid = 50
#print(baseURL+'&field=%s&field2=%s'% (temp, umd))
 
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22
 
GPIO.setmode(GPIO.BOARD)
 
# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25
 
# Informacoes iniciais
print ("*** Lendo os valores de temperatura e umidade")
 
while(1):
   # Efetua a leitura do sensor
   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
   # Caso leitura esteja ok, mostra os valores na tela
   if umid is not None and temp is not None:
     print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}n".format(temp, umid))
     conn= urllib.request.urlopen(baseURL + '&field1=%s&field2=%s'  % (temp,umid))
     conn.close()
     print ("Aguarda 5 segundos para efetuar nova leitura...")
     
     time.sleep(5)
   else:
     # Mensagem de erro de comunicacao com o sensor
     print("Falha ao ler dados do DHT11 !!!")# Programa : Sensor de temperatura DHT11 com Raspberry Pi