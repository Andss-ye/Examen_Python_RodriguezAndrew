# Importo lo necesario
import datetime
from .validaciones import validarIdentificacion, validarVacio
fecha = str(datetime.date.today())      

#  Funcion para registrar los empleados
def registrarEmpleado(empleados):
    identificacion = validarIdentificacion(str(input('\nEscriba el numero de identificacion del empleado: ')))

    if identificacion not in empleados:
        nombre = validarVacio(str(input('\nEscriba el nombre del empleado a registrar: ')))
        cargo = validarVacio(str(input('\nCual es el cargo en el que esta el empleado: ')))
        salario =  float(input('\nEscriba el salario del empleado: $'))
        empleados[identificacion] = {
            'nombre': nombre,
            'cargo': cargo,
            'salario': salario,
            'inasistencias': [],
            'bonos': []
        }

        print(f'\nEl empleado {nombre} ha sido registrado con exito!!!')
        return empleados
    
    else:
        print('\nEl empleado ya se encuentra registrado, revise los datos que ingreso')
        return empleados
    
# funcion para registrar las inasistencias
def registroInasistencias(empleados):
    identificacion = str(input('\nEscriba el numero de identificacion del empleado que falto el dia de hoy al trabajo: '))

    if identificacion in empleados:
        opc = str(input('\nDesea registrar la inasistencia del empleado? (S/N): '))

        if fecha in empleados[identificacion]['inasistencias']:
            print(f'\nEl empleado {empleados[identificacion]['nombre']} ya se encuentra registrado con inasistencia para la fecha del dia de hoy')
            return empleados

        if opc.upper() == 'S':
            empleados[identificacion]['inasistencias'].append(fecha)
            print(f'\nLa inasistencia del empleado {empleados[identificacion]["nombre"]} se registro correctamente')
            return empleados

        else:
            print('\nNo se registro la inasistencia del empleado')
            return empleados
        
    else:
        print('\nEl empleado no se encuentra registrado')
        return empleados
    
# funcion para registrar los bonos
def registroBonos(empleados):
    identificacion = str(input('\nEscriba el numero de identificacion del empleado que recibira el bono: '))

    if identificacion in empleados:
        valor = int(input(f'\nEscriba el valor del bono del empleado {empleados[identificacion]['nombre']}: $'))
        concepto = str(input('\nDe que es el bono, escriba una descripcion o el nombre del bono: '))

        empleados[identificacion]['bonos'].append({
            'valor': valor,
            'concepto': concepto
        })
        print(f'\nEl bono del empleado {empleados[identificacion]["nombre"]} se ha registrado correctamente')
        return empleados
    
    else:
        print(f'\nNo se encuentra registrado ese empleado con ese numero de identificacion')
        return empleados