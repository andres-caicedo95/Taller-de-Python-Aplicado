# Crear la lista de inventario
inventario = []

# Agregar componentes al inventario
componente1 = {
    "id": "S-101",
    "tipo": "Sensor",
    "ubicacion": "Sala A",
    "lecturas": [23.5, 24.1, 22.8]
}

componente2 = {
    "id": "M-205", 
    "tipo": "Motor",
    "ubicacion": "Planta B",
    "lecturas": [45.2, 46.8, 44.9]
}

componente3 = {
    "id": "V-307",
    "tipo": "Válvula", 
    "ubicacion": "Sistema C",
    "lecturas": [12.3, 11.9, 12.7]
}

# Añadir componentes a la lista
inventario.append(componente1)
inventario.append(componente2)
inventario.append(componente3)

# Mostrar el inventario completo
print("=== INVENTARIO DE COMPONENTES ===")
for componente in inventario:
    print(f"ID: {componente['id']}")
    print(f"Tipo: {componente['tipo']}")
    print(f"Ubicación: {componente['ubicacion']}")
    print(f"Lecturas: {componente['lecturas']}")
    print("-" * 20)

# Función para calcular promedio de lecturas
def calcular_promedio(id_buscar):
    for componente in inventario:
        if componente["id"] == id_buscar:
            lecturas = componente["lecturas"]
            promedio = sum(lecturas) / len(lecturas)
            return promedio
    return None

# Calcular promedio para un componente específico
print("\n=== CÁLCULO DE PROMEDIO ===")
id_buscar = "S-101"
promedio = calcular_promedio(id_buscar)

if promedio is not None:
    print(f"Promedio de lecturas para {id_buscar}: {promedio:.2f}")
else:
    print(f"Componente {id_buscar} no encontrado")