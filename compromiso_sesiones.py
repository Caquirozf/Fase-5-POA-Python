# Matriz: [ID Cliente, Duración (segundos), Eventos Clics]
sesiones = [
    [101, 250, 12],
    [102, 45, 2],
    [103, 120, 5],
    [104, 190, 4],
    [105, 30, 10]
]


def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


print("Informe de compromiso por sesión")
for fila in sesiones:
    id_cliente = fila[0]
    duracion = fila[1]
    clics = fila[2]
    clasificacion = clasificar_compromiso(duracion, clics)
    print(f"Cliente {id_cliente}: {clasificacion}")
