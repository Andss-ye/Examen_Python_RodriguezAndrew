import json

# obtener o cargar datos de empleados
def getDataEmpleados():
    try:
        with open('bd/empleados.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    
# guardar los datos de los empleados
def SaveDataEmpleados(empleados):
    with open('bd/empleados.json',  'w') as file:
        json.dump(empleados, file, indent=4)

# crear los archivos de nomina
def saveNomina(nomina):
    for id in nomina:
        empleado = {}
        empleado[id] = nomina[id]
        with open(f'bd/nomina_{nomina[id]['nombre']}.json', 'w') as file:
            json.dump(empleado, file, indent=4)