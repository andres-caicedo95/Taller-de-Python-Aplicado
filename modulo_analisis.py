# inventario

inventario = [
    {"id": "T-21", "tipo": "Sensor", "ubicacion": "Planta_Norte", "lecturas": [45.8, 46.1, 44.9]},
    {"id": "P-10", "tipo": "Sensor", "ubicacion": "Planta_Sur", "lecturas": [30.2, 31.0, 29.8]},
    {"id": "M-33", "tipo": "Motor", "ubicacion": "Planta_Norte", "lecturas": [55.0, 54.5, 56.1]},
    {"id": "S-11", "tipo": "Sensor", "ubicacion": "Planta_Norte", "lecturas": [49.2, 50.0, 48.8]}
]

# Función: analizar_componente()

def analizar_componente(componente_dict):
    """
    Recibe un diccionario de componente.
    Calcula promedio, máximo y mínimo de las lecturas.
    Retorna un nuevo diccionario con los resultados.
    """
    lecturas = componente_dict["lecturas"]
    promedio = sum(lecturas) / len(lecturas)
    maximo = max(lecturas)
    minimo = min(lecturas)

    return {"promedio": promedio, "max": maximo, "min": minimo}


# Probamos la función con uno de los componentes:
print("*** ANÁLISIS DE COMPONENTE ***")
resultado = analizar_componente(inventario[0])
print(f"ID: {inventario[0]['id']}")
print(resultado)

# Filtrado: sensores tipo "Sensor" y ubicación "Planta_Norte"
sensores_criticos = list(filter(
    lambda comp: comp["tipo"] == "Sensor" and comp["ubicacion"] == "Planta_Norte",
    inventario
))

# Mapeo: obtener solo los IDs de esos sensores
ids_sensores = list(map(lambda comp: comp["id"], sensores_criticos))

print("\n*** SENSORES CRÍTICOS ***")
print("IDs:", ids_sensores)
