# Práctica P3: Recorrido Secuencial de LEDs

## Introducción

En esta práctica se implementó un sistema de iluminación secuencial utilizando una Raspberry Pi y el lenguaje de programación Python. El objetivo principal es controlar cinco LEDs conectados a diferentes pines GPIO para crear un efecto de recorrido.

Los LEDs se activan uno después de otro siguiendo una dirección y posteriormente realizan el recorrido en sentido contrario. De esta manera se obtiene un efecto visual similar al movimiento de un cursor.

Para realizar la práctica se utilizó una conexión remota mediante SSH. El código fue desarrollado y ejecutado desde una máquina virtual con Fedora utilizando VirtualBox, mientras que la Raspberry Pi funcionó como el dispositivo encargado de controlar los componentes electrónicos.

---

## Objetivo

Desarrollar un programa en Python que permita controlar varios LEDs mediante los puertos GPIO de una Raspberry Pi, utilizando una estructura de datos para almacenar los pines y ciclos de repetición para realizar el encendido y apagado automático.

También se busca familiarizarse con:

* El uso de los GPIO de la Raspberry Pi.
* La programación en Python.
* El manejo de listas y ciclos `for`.
* La conexión remota mediante SSH.
* La configuración de salidas digitales.

---

## Material utilizado

Para realizar esta práctica se utilizaron los siguientes elementos:

* Raspberry Pi.
* 5 LEDs.
* Resistencias para los LEDs.
* Protoboard.
* Cables de conexión.
* Computadora.
* Máquina virtual Fedora.
* VirtualBox.
* Python.
* Librería `RPi.GPIO`.
* Conexión de red para utilizar SSH.

---

## Configuración de los LEDs

Los cinco LEDs fueron conectados utilizando la numeración BCM de la Raspberry Pi.

| LED   | GPIO BCM | Pin físico | Configuración |
| ----- | -------: | ---------: | ------------- |
| LED 1 |       18 |         12 | Salida        |
| LED 2 |       23 |         16 | Salida        |
| LED 3 |       24 |         18 | Salida        |
| LED 4 |       25 |         22 | Salida        |
| LED 5 |        8 |         24 | Salida        |

Cada GPIO funciona como una salida digital encargada de proporcionar la señal necesaria para encender o apagar el LED correspondiente.

---

## Conexión con la Raspberry Pi

Para trabajar con la Raspberry Pi de manera remota se utilizó el protocolo SSH desde Fedora.

La conexión se realizó mediante:

```bash
ssh mar@192.168.50.83
```

Después de establecer la conexión, se ingresó al entorno de trabajo de Python mediante:

```bash
source 8S11/bin/activate
```

Al activarse correctamente, la terminal muestra el nombre del entorno virtual al principio de la línea de comandos.

---

## Creación y ejecución del programa

El archivo utilizado para almacenar el programa fue:

```text
recorridoLedVector.py
```

Para modificar el archivo se utilizó:

```bash
sudo nano recorridoLedVector.py
```

Posteriormente se ejecutó el programa mediante:

```bash
python recorridoLedVector.py
```

El programa permanece funcionando hasta que el usuario presiona `Ctrl+C`.

---

## Funcionamiento del programa

El programa utiliza una lista para almacenar los números correspondientes a los GPIO:

```python
LED_PIN = [18, 23, 24, 25, 8]
```

Esta estructura permite trabajar con todos los LEDs sin tener que configurar cada uno individualmente.

Primero se establece la numeración BCM:

```python
GPIO.setmode(GPIO.BCM)
```

Después, los pines de la lista son configurados como salidas y comienzan en estado apagado:

```python
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
```

Una vez configurados los GPIO, comienza el ciclo principal del programa.

### Recorrido hacia adelante

El primer ciclo recorre los elementos de la lista desde el primero hasta el último:

```text
18 → 23 → 24 → 25 → 8
```

Cada LED permanece encendido durante un segundo y posteriormente se apaga.

### Recorrido hacia atrás

Después de terminar el primer recorrido, el programa utiliza la lista en sentido inverso:

```text
8 → 25 → 24 → 23 → 18
```

Esto genera el efecto de ida y vuelta entre los cinco LEDs.

El proceso se encuentra dentro de un `while True`, por lo que la secuencia continúa repitiéndose de manera indefinida.

---

## Control de la interrupción

Para evitar que el programa termine de forma incorrecta cuando el usuario quiera detenerlo, se utiliza:

```python
except KeyboardInterrupt:
```

Esto permite detectar la combinación `Ctrl+C`.

Cuando se realiza la interrupción, el programa muestra un mensaje indicando que fue detenido por el usuario.

---

## Liberación de los GPIO

Al finalizar el programa se utiliza:

```python
GPIO.cleanup()
```

Esta instrucción libera los pines que fueron utilizados durante la ejecución.

Es importante realizar esta limpieza para evitar que los GPIO permanezcan configurados y puedan ocasionar conflictos cuando se ejecute otro programa posteriormente.

---

## Resultado obtenido

Como resultado se obtuvo una secuencia automática de iluminación en la que los cinco LEDs se encienden individualmente.

El recorrido comienza desde el primer LED y avanza hasta el último. Después, la dirección cambia y los LEDs se activan nuevamente en sentido contrario.

El efecto final puede representarse de la siguiente manera:

```text
LED 1 → LED 2 → LED 3 → LED 4 → LED 5
LED 5 → LED 4 → LED 3 → LED 2 → LED 1
                  ↻
              REPETIR
```

De esta forma se consigue un recorrido continuo mientras el programa permanece activo.

---

## Conclusión

La práctica permitió comprobar el funcionamiento de las salidas GPIO de una Raspberry Pi mediante un programa desarrollado en Python.

El uso de una lista facilitó la administración de los cinco LEDs, ya que los pines pudieron recorrerse mediante ciclos en lugar de escribir instrucciones independientes para cada componente.

Además, la actividad permitió practicar la conexión SSH, el uso de un entorno virtual de Python y la programación básica de dispositivos electrónicos mediante GPIO.

Finalmente, se comprobó que la Raspberry Pi puede utilizarse para controlar diferentes componentes electrónicos a partir de instrucciones programadas, creando secuencias de iluminación de manera automática.
