# ==========================================
# PROBLEMA 1: Clasificación de compromiso
# ==========================================

# Matriz con los datos:
# [ID Cliente, Duración en segundos, Eventos Clics]

sesiones = [
    ["C001", 240, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 200, 9],
    ["C005", 75, 1]
]

# ------------------------------------------
# Función para clasificar el compromiso
# ------------------------------------------
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# ------------------------------------------
# Función para generar el informe
# ------------------------------------------
def generar_informe(matriz):
    print("INFORME DE COMPROMISO DE CLIENTES")
    print("-" * 40)

    # Recorrer cada sesión
    for sesion in matriz:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        # Obtener clasificación
        clasificacion = clasificar_compromiso(duracion, clics)

        # Mostrar resultado
        print("ID Cliente:", id_cliente)
        print("Clasificación:", clasificacion)
        print("-" * 40)

# ------------------------------------------
# Programa principal
# ------------------------------------------
generar_informe(sesiones)