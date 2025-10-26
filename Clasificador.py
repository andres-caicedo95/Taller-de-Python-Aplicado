print("CLASIFICADOR DE INVENTARIO")

# Lista de inventario
inventario = [
    {"id": "S001", "tipo": "sensor", "nombre": "Sensor Temperatura"},
    {"id": "M001", "tipo": "motor", "nombre": "Motor DC"},
    {"id": "V001", "tipo": "valvula", "nombre": "Válvula Control"},
    {"id": "S002", "tipo": "sensor", "nombre": "Sensor Presión"},
    {"id": "M002", "tipo": "motor", "nombre": "Motor Paso a Paso"},
    {"id": "V002", "tipo": "valvula", "nombre": "Válvula Seguridad"}
]

# Listas vacías para clasificar
sensores = []
motores = []
valvulas = []

# Clasificar componentes
for componente in inventario:
    tipo = componente["tipo"]
    
    if tipo == "sensor":
        sensores.append(componente["id"])
    elif tipo == "motor":
        motores.append(componente["id"])
    elif tipo == "valvula":
        valvulas.append(componente["id"])

# Mostrar resultados
print(f"Sensores: {sensores}")
print(f"Motores: {motores}")
print(f"Válvulas: {valvulas}")


print("EJERCICIO 2: SIMULADOR DE LLENADO DE TANQUE")

# Configuración inicial
volumen_actual = 0
tasa_flujo = 50.5
minuto = 0

print("Inicio simulación")

# Simular llenado
while volumen_actual < 1000:
    minuto += 1
    volumen_actual += tasa_flujo
    
    if volumen_actual > 950:
        print(f"Minuto {minuto}: {volumen_actual:.1f} litros - ALERTA: Tanque casi lleno")
        break
    
    print(f"Minuto {minuto}: {volumen_actual:.1f} litros")

print("Simulación de llenado detenida.")