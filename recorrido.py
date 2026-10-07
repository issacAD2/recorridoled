import RPi.GPIO as GPIO # type: ignore
from time import sleep

# Pines de los LEDs
LEDS = (18, 23, 24, 25, 8)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configuración de los pines
for pin in LEDS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def encender_led(pin):
    GPIO.output(pin, GPIO.HIGH)
    print("LED en GPIO", pin, "-> ENCENDIDO")
    sleep(1)

    GPIO.output(pin, GPIO.LOW)
    print("LED en GPIO", pin, "-> APAGADO")
    sleep(0.5)


def secuencia():
    # Recorrido de izquierda a derecha
    for pin in LEDS:
        encender_led(pin)

    # Recorrido de derecha a izquierda
    for pin in LEDS[::-1]:
        encender_led(pin)


try:
    print("================================")
    print("   SECUENCIA DE LEDs - RPi")
    print("================================")
    print("GPIO utilizados:", LEDS)
    print("Presiona Ctrl+C para detener")

    while True:
        secuencia()

except KeyboardInterrupt:
    print("\nPrograma detenido.")

finally:
    GPIO.output(LEDS, GPIO.LOW) if False else None
    GPIO.cleanup()
    print("Pines GPIO liberados correctamente.")