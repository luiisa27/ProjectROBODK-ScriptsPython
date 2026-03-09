# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project

# You can also use the new version of the API:
from robodk import robolink, robomath
import time

RDK = robolink.Robolink()

frame_cinta = RDK.Item('cinta2')

INCREMENTO_MM = 50
PASOS_MAXIMOS = 33
DELAY = 0.05

print("Cinta en ejecución continua")

# Diccionario para llevar el progreso de cada caja
progreso = {}

while True:
    for caja in frame_cinta.Childs():
        name = caja.Name()

        # Solo cajas cerradas visibles
        if 'caja_cerrada' in name and caja.Visible():

            # Si es la primera vez que vemos esta caja inicializamos sus pasos
            if name not in progreso:
                progreso[name] = 0

            # Si aún no ha llegado al límite de pasos, avanza
            if progreso[name] < PASOS_MAXIMOS:

                pose = caja.Pose()
                pose = pose * robomath.transl(0, INCREMENTO_MM, 0)
                caja.setPose(pose)

                progreso[name] += 1

            else:
                # Cuando llega al límite se oculta
                caja.setVisible(False)
                print(name, "ocultada")

    time.sleep(DELAY)
