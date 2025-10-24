# Variables y Tipos de Datos
fuerza_aplicada = 1500.5  # float (Newtons)
area_seccion = 20       # int (mm^2)
material = "Acero 1020"  # str
es_seguro = False        # bool

# Operadores Aritméticos
# Esfuerzo (Stress) = Fuerza / Área
esfuerzo = fuerza_aplicada / area_seccion

print(f"Material: {material}")
print(f"Esfuerzo Aplicado: {esfuerzo} MPa") # MPa = N/mm^2

# Operadores Lógicos y de Comparación
limite_fluencia = 250.0  # Límite de seguridad en MPa
es_seguro = esfuerzo < limite_fluencia

print(f"¿El diseño es seguro? {es_seguro}")
