from machine import Pin, I2C, PWM, RTC # Librerías que son las herramientas que necesitamos (importamos pines, pantalla, sonido y reloj)

import ssd1306 # el controlador visual de pantalla OLED de 128x32
import time    
import network   # herramienta para encender la antena WiFi
import urequests #herramienta para enviar el mensaje por internet

# 1. Configuracion basica (Pines y Componentes)

hall_sensor = Pin(34, Pin.IN, Pin.PULL_UP) # Configuración de Pin 34 para leer el sensor magnético de la tapa (1=Abierto, 0=Cerrado)

boton_silencio = Pin(15, Pin.IN, Pin.PULL_UP)

buzzer = PWM(Pin(25), freq=1000, duty=0)# Configuracion de Pin 25 para el Buzzer, con tono de 1000Hz y volumen inicial en 0 (apagado)

i2c = I2C(0, scl=Pin(22), sda=Pin(21))#la comunicación con la pantalla OLED (SCL en pin 22, SDA en pin 21)

display = ssd1306.SSD1306_I2C(128, 32, i2c)#resolución exacta: 128 de ancho por 32 de alto


pines_leds = [13, 12, 14, 27, 26, 32, 33]# Los 7 pines donde conectaremos los LEDs de los días en una lista

leds = [] #caja vacía para organizar los LEDs

for pin in pines_leds:      # Buscamos en la lista y configuramos cada pin como salida de energía (OUT)
    leds.append(Pin(pin, Pin.OUT))

# 2. Conexion a Internet
def conectar_wifi():
    
    wlan = network.WLAN(network.STA_IF)# Objeto para controlar la antena de la placa
    # Encendemos la antena físicamente
    wlan.active(True)
    
    if not wlan.isconnected():
        print("Buscando red WiFi...")
        display.fill(0)
        display.text("CONECTANDO WIFI..", 0, 10)
        display.show()
        
        wlan.connect("NOMBRE_DE_TU_CELULAR", "CONTRASEÑA_DEL_CELULAR") #Ingresa datos del internet compartido con celular
        
        while not wlan.isconnected():# Esperando hasta que la conexión sea exitosa
            pass 
            
    print("¡Conectado a Internet exitosamente!")

conectar_wifi()

# 3. Envio de mensaje (Alerta a WhatsApp)
def enviar_mensaje_real():

    numero = "+56912345678" # Número del cuidador
    api_key = "123456" # Clave secreta que te da la página de CallMeBot       
    texto = "EMERGENCIA:+El+paciente+no+consumio+su+pastilla."
    url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={texto}&apikey={api_key}" #el enlace completo
    
    try:
        respuesta = urequests.get(url)
        if respuesta.status_code == 200:# Si el servidor responde '200' es correcto
            print("¡Alerta enviada al cuidador!")
        respuesta.close()
    except:
        print("Error: No se pudo enviar el mensaje por falta de red.")


# 4. Configuración de reloj y sus horarios
rtc = RTC() #reloj interno de placa
rtc.datetime((2026, 6, 22, 0, 7, 29, 50, 0))# Fijamos una hora prueba: Día Lunes (0), a las 07:29:50 para probar rápido

alarma_activa = False   # ¿Estamos en la media hora de espera?
pastilla_tomada = False # sirve si se abrió la tapa
sms_enviado = False     # Evita mandar muchos mensajes seguidos
alarma_silenciada = False

nombres_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

horas_dosis = [0, 8, 16]# Las horas exactas donde debe tomar la pastilla
horas_pre = [23, 7, 15]# Las horas donde da el aviso preventivo de "faltan 30 minutos"

# Borramos pantalla y damos mensaje de bienvenida al encender
display.fill(0) 
display.text("SISTEMA INICIADO", 0, 10) 
display.show()  
time.sleep(2)   

# 5. Bucle principal
while True:
    
    _, _, _, dia_semana, hora, minuto, segundo, _ = rtc.datetime()
    estado_tapa = hall_sensor.value() # Leemos si la tapa está abierta (1) o cerrada (0)
    estado_boton = boton_silencio.value()
    
    display.fill(0)# Borramos la pantalla nueva imagen
    
    if hora in horas_pre and minuto == 30 and segundo < 10:# Aviso 30 minutos antes (dura 10 segundos)
        display.text("AVISO PREVENTIVO", 0, 0)
        display.text("Dosis en 30 min", 5, 15)
        
        if segundo % 2 == 0: # Efecto parpadeo: si el segundo es par (0, 2, 4...)
            leds[dia_semana].value(1) # Prende la luz del día actual
            buzzer.duty(512)          # Suena a la mitad de volumen
        else: 
            leds[dia_semana].value(0) # Apaga luz
            buzzer.duty(0)            # Apaga sonido
            
        display.show()   
        time.sleep(0.1)  
        continue # Vuelve al inicio del bucle ignorando el resto del código

    if hora in horas_dosis and minuto == 0 and segundo == 0:# Caso pricipal: Inicia la hora de la toma (8:00, 12:00, 16:00)
        alarma_activa = True    # Activamos la espera
        pastilla_tomada = False # Reseteamos el intento
        sms_enviado = False     # Reseteamos el bloqueo de SMS
        alarma_silenciada = False

    sonando_principal = (hora in horas_dosis and minuto == 0 and segundo < 15)# Variable correcta durante 15 segundos de la hora

    if estado_boton == 0 and alarma_activa == True:
        alarma_silenciada = True

    # Si la tapa se abre (1) y la alarma está esperando (True)...
    if estado_tapa == 1 and alarma_activa == True:
        pastilla_tomada = True    # Marcamos el éxito
        alarma_activa = False     # Cerramos la ventana de espera
        buzzer.duty(0)            # Callamos el ruido inmediatamente
        leds[dia_semana].value(0) # Apagamos el LED del día

    if hora in horas_dosis and minuto == 30 and segundo == 0:# Pasaron 30 minutos desde la horario predeterminado
        alarma_activa = False # Se acabó el tiempo
        
        if pastilla_tomada == False and sms_enviado == False:# Si nunca registró la apertura y aún no mandamos el mensaje
            print(f" Alerta de las {hora}:00 sin tomar.")
            # Disparamos el mensaje usando el WiFi
            enviar_mensaje_real() 
            sms_enviado = True # Bloqueamos para que no envíe mensajes

    if alarma_activa and sonando_principal and not pastilla_tomada:   # Estado 1: Sonando fuerte (Primeros 15 segundos)
        if not alarma_silenciada:
            if segundo % 2 == 0:  
                leds[dia_semana].value(1)
                buzzer.duty(512)
            else:
                leds[dia_semana].value(0)
                buzzer.duty(0)
                
            display.text("HORA DE DOSIS", 5, 0)  # Fila de arriba
            display.text("Abra la tapa", 15, 15)   # Fila de abajo
        else:
            leds[dia_semana].value(0)
            buzzer.duty(0)
            display.text("SILENCIADO", 25, 0)
            display.text("Abra la tapa", 15, 15)

    elif alarma_activa and not sonando_principal and not pastilla_tomada:# Estado 2: Alarma silenciosa esperando que abra (Hasta los 30 min)
        leds[dia_semana].value(0) # Mantenemos luz apagada
        buzzer.duty(0)            # Mantenemos silencio absoluto
        display.text("PENDIENTE..", 20, 0)
        display.text("Abra la tapa", 15, 15)
    
    elif pastilla_tomada and (hora in horas_dosis) and minuto < 30: # Estado 3: Exito (Se queda hasta el minuto 30)
        leds[dia_semana].value(0)
        buzzer.duty(0)
        display.text("DOSIS REGISTRADA", 0, 0)
        display.text("Gracias", 35, 15)
        
    else:
        str_hora = "{:02d}:{:02d}:{:02d}".format(hora, minuto, segundo) # Formateamos hora para luzca como reloj digital
        
        display.text(nombres_dias[dia_semana], 0, 0) # Fila 1 (Altura 0)
        display.text(str_hora, 0, 12)                # Fila 2 (Altura 12)
        
        # Calculamos lógicamente qué hora será el próximo aviso
        if hora < 8:
            display.text("Prox: 08:00", 0, 24)       # Fila 3 (Altura 24)
        elif hora < 16:
            display.text("Prox: 16:00", 0, 24)       # Fila 3 (Altura 24)
        else:
            display.text("Prox: 00:00", 0, 24) # Mañana siguiente
            
        leds[dia_semana].value(0)
        buzzer.duty(0)

    display.show()
    time.sleep(0.1)# Pequeño descanso de 0.1s al procesador antes de reiniciar el bucle