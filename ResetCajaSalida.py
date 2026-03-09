# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project

# You can also use the new version of the API:
# ResetCajas.py
# Borra todas las cajaplaceX.0 y oculta/recoloca todas las caja_cerrada_X

from robodk import robolink
RDK = robolink.Robolink()

# 1. Obtener el frame padre correcto
sis = RDK.Item('SisGeneral')
if not sis.Valid():
    raise Exception("No existe el frame 'SisGeneral' ")

# 2. Obtener todos los objetos de la estación
lista = RDK.ItemList()

for item in lista:
    try:
        name = item.Name()
    except:
        continue

    # Borra TODAS las cajaplaceX.0
    if 'cajaplace' in name:
        item.Delete()
        continue

    # Resetea TODAS las caja_cerrada_X
    if 'caja_cerrada_' in name:
        # 1. Ocultar
        item.setVisible(False)

        # 2. Recolocar como hija de SisGeneral
        item.setParent(sis)

print("Reset completado: cajaplace eliminadas y cajas cerradas ocultas en SisGeneral.")
