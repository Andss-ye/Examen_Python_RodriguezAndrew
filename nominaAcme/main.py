# Importo los modulos necesarios para hacer la ejecucion del programa
from modulos.fileManager import getDataEmpleados, SaveDataEmpleados, saveNomina
from modulos.empleadoManager import registrarEmpleado, registroInasistencias, registroBonos
from modulos.nomina import calculoNominas

# Funcion que sirve para mostrar el menu y retornar la opc escogida
def menu():
    print('''
========= BIENVENIDO =========          

1. Registrar empleado
2. Registro de inasistencias
3. Registro de bonos - extra legales
4. Calculo de nomina de empleados
0. Salir
''')
    opc = int(input('\nEscoja la opcion deseada: '))
    return opc

# Se obtienen los datos de los empleados
empleados = getDataEmpleados()

# Sirve para inicializar el ciclo del programa
opc = 10

while opc != 0:
    try:
        opc = menu()
        # Registrar empleados
        if opc == 1:
            print('Registrar empleado')
            empleados = registrarEmpleado(empleados)
            SaveDataEmpleados(empleados)

        # Registrar inasistencias
        elif opc == 2:
            print('Registro de inasistencias')
            empleados = registroInasistencias(empleados)
            SaveDataEmpleados(empleados)
        
        # Registro de bonos
        elif opc == 3:
            print('Registro de bonos extra legales')
            empleados = registroBonos(empleados)
            SaveDataEmpleados(empleados)
        
        # Calculo de nominas
        elif opc == 4:
            print('Calculo de nomina de empleados')
            nominas = calculoNominas(empleados)
            saveNomina(nominas)
        
        # Cerrar el programa
        elif opc == 0:
            print('Gracias por utilizar el sistema')
            exit()

        else:
            print('\nDato no valido, escoja un numero de 0 a 4')
    
    # Por si el user ingresa un dato no valido
    except ValueError:
        print('\nDato no valido, el dato tiene que ser numerico')

    except KeyboardInterrupt:
        print('\nSaliendo del sistema')
        exit()