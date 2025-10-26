
# Reporte recibido
reporte = "ID_SENSOR:T-21,LOC:Planta_Norte,TEMP:45.8,STATUS:OK"

# Separar por comas
partes = reporte.split(',')

# Extraer valores con split(':')
id_sensor = partes[0].split(':')[1]
ubicacion = partes[1].split(':')[1]
temperatura = float(partes[2].split(':')[1])
estado = partes[3].split(':')[1]

# Imprimir reporte formateado
print("REPORTE DE SENSOR:")
print(f"ID: {id_sensor}")
print(f"Ubicación: {ubicacion}")
print(f"Temperatura: {temperatura} °C")
print(f"Estado: {estado}")


# Validador de Lote

def validar_codigo_lote(codigo_lote):
    # Verificar largo
    if len(codigo_lote) != 12:
        return False
    # Verificar prefijo y sufijo
    if not codigo_lote.startswith("LOT-"):
        return False
    if not codigo_lote.endswith("-24"):
        return False
    # Verificar 8vo carácter (índice 7)
    if codigo_lote[7] not in ("X", "Y"):
        return False
    return True

# Pruebas
codigos = ["LOT-45A-X-B-24", "LOT-44B-Z-C-23"]

print("\nVALIDACIÓN DE LOTES:")
for codigo in codigos:
    if validar_codigo_lote(codigo):
        print(f"{codigo}: Válido")
    else:
        print(f"{codigo}: Inválido")
