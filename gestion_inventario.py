# gestion_inventario.py - VERSIÓN COMPLETA Y SIMPLE

print("=== SISTEMA DE GESTIÓN ===")

# PARTE 1: INVENTARIO
print("\n1. INVENTARIO DE COMPONENTES")

# Crear inventario
inventario = [
    {"id": "S-101", "tipo": "Sensor", "ubicacion": "Sala A", "lecturas": [23.5, 24.1, 22.8]},
    {"id": "M-205", "tipo": "Motor", "ubicacion": "Planta B", "lecturas": [45.2, 46.8, 44.9]},
    {"id": "V-307", "tipo": "Válvula", "ubicacion": "Sistema C", "lecturas": [12.3, 11.9, 12.7]}
]

# Mostrar inventario
for comp in inventario:
    print(f"ID: {comp['id']}, Tipo: {comp['tipo']}, Lecturas: {comp['lecturas']}")

# Calcular promedio para S-101
print("\n2. PROMEDIO DE LECTURAS")
id_buscar = "S-101"
for comp in inventario:
    if comp["id"] == id_buscar:
        promedio = sum(comp["lecturas"]) / 3
        print(f"Promedio de {id_buscar}: {promedio:.2f}")
        break

# PARTE 2: EXPERIMENTOS
print("\n3. ANÁLISIS DE EXPERIMENTOS")

# Conjuntos de experimentos
equipo_A = {("EXP-001", "2023-10-01"), ("EXP-002", "2023-10-02"), ("EXP-003", "2023-10-03")}
equipo_B = {("EXP-002", "2023-10-02"), ("EXP-004", "2023-10-04"), ("EXP-001", "2023-10-01")}

# Operaciones con conjuntos
en_comun = equipo_A & equipo_B  # Intersección
todos = equipo_A | equipo_B     # Unión
solo_A = equipo_A - equipo_B    # Diferencia

# Resultados
print("Experimentos en común:", en_comun)
print("Todos los experimentos:", todos)
print("Solo Equipo A:", solo_A)

print("\n=== FIN DEL PROGRAMA ===")