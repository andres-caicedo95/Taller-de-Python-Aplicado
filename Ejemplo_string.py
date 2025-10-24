
# Los IDs de componentes a menudo tienen información estructurada
id_componente = "SN-AFT-1035-B2"

# Slicing (rebanado)
tipo_componente = id_componente[3:6] # 'AFT'
numero_serie = id_componente[7:11] # '1035'

# Métodos de String
if id_componente.startswith("SN-"):
    print("ID de Serial válido.")

# f-strings para formatear
reporte = f"Componente: {tipo_componente}, Serie: {numero_serie}"
print(reporte)

# split() para dividir
data_log = "ERROR,Sensor_Temp,Valor_Alto,45.5"
partes_log = data_log.split(',')
print(f"Tipo de Log: {partes_log[0]}") # 'NO VALIDO'
