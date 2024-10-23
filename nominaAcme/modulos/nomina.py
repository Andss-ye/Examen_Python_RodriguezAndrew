def calculoNominas(empleados):
    nominas = {}        # dict vacio para almacenar los datos de las nominas
    diasMes = 30
    salarioMin = 1000000    # sal minimo para operar

    # recorrer los empleados para sacar los datos de cada uno y por lo tanto hacer los calculos
    for id, info in empleados.items():
        salarioEmpleado = info['salario']
        inasistencias = info['inasistencias']
        bonos = info['bonos']
        valorDiaTrabajo = salarioEmpleado / diasMes

        auxilioTransporte = 0
        conceptoSalud = salarioEmpleado * 0.04
        conceptoPension = salarioEmpleado * 0.04
        faltasTrabajo = (valorDiaTrabajo  * len(inasistencias))

        if salarioEmpleado < (salarioMin * 2):
            auxilioTransporte = salarioEmpleado * 0.1

        totalBonos = 0
        totalDescuentos = (conceptoPension + conceptoSalud +  faltasTrabajo)

        for bono in bonos:
            totalBonos += bono['valor']

        salarioFinal = (salarioEmpleado - totalDescuentos) + totalBonos + auxilioTransporte
        
        nominas[id] = {
            'nombre':  info['nombre'],
            'cargo': info['cargo'],
            'salario': salarioEmpleado,
            'descuento por pension': conceptoPension,
            'descuento por salud': conceptoSalud,
            'descuento por faltas al trabajo': faltasTrabajo,
            'auxilio de transporte':  auxilioTransporte,
            'total bonos extralegales': totalBonos,
            'salario final': salarioFinal
        }

    print('Nominas calculadas y guardadas')
    return nominas