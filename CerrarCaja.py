# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project

# You can also use the new version of the API:


from robodk import robolink
RDK = robolink.Robolink()

robot = RDK.Item('UR5 SalidaCjas')
tool  = RDK.Item('VentosaSalida')

# 1. Encontrar la caja abierta agarrada (la cajaplace VISIBLE unida a la ventosa)
hijos = tool.Childs()
caja_abierta = None

for item in hijos:
    try:
        name = item.Name()
    except:
        continue

    # Debe ser una cajaplace y estar visible 
    if 'cajaplace' in name and item.Visible():
        caja_abierta = item
        break

if caja_abierta is None:
    raise Exception("No hay ninguna cajaplace VISIBLE agarrada por la ventosa.")

# 2. Buscar una caja cerrada libre (precreada y oculta en SisGeneral)
lista = RDK.ItemList()
caja_cerrada = None

for item in lista:
    try:
        name = item.Name()
    except:
        continue

    if 'caja_cerrada_' in name:
        # Debe estar oculta y no ser hija del tool
        if not item.Visible() and item.Parent().Name() != tool.Name():
            caja_cerrada = item
            break

if caja_cerrada is None:
    raise Exception("No hay cajas cerradas libres. Crea más en la estación.")

# 3. Colocar la caja cerrada en la misma pose que la abierta
pose_abierta = caja_abierta.Pose()
caja_cerrada.setPose(pose_abierta)

# 4. Hacerla hija de la ventosa
caja_cerrada.setParent(tool)

# 5. Mostrar la caja cerrada
caja_cerrada.setVisible(True)

# 6. Ocultar SOLO la cajaplace que estaba en la ventosa en este ciclo
caja_abierta.setVisible(False)

print("Caja cerrada activada:", caja_cerrada.Name())
