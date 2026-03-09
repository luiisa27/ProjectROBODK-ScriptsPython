# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project

# You can also use the new version of the API:

from robodk import robolink
import time

RDK = robolink.Robolink()

sensor = RDK.Item('sensorDetectaCajaSalida')

print("Sensor activo. Esperando cajas...")

caja_detectada = None
estado_anterior = 0

while True:

    # Buscar todas las cajas tipo cajaplaceX.0
    items = RDK.ItemList()

    # Buscar la caja que esté dentro del sensor
    caja_actual = None
    for item in items:
        name = item.Name()
        if 'cajaplace' in name and item.Visible():
            if sensor.Collision(item):
                caja_actual = item
                break

    # Si hay caja dentro del sensor
    detectado = 1 if caja_actual is not None else 0

    # Cambio de estado
    if detectado != estado_anterior:

        # Cuando DETECTA una caja
        if detectado == 1:
            caja_detectada = caja_actual
            print("Caja detectada:", caja_detectada.Name())
            RDK.RunProgram("Prog_cajasSalida")

        # Cuando la caja SALE del sensor
        else:
            print("Caja retirada. Esperando siguiente caja...")

        estado_anterior = detectado

    time.sleep(0.01)
