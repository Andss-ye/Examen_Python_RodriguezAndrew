# valida ell numero de identificacion
def validarIdentificacion(identificacion):
    while True:
        if identificacion.isdigit():
            return identificacion
        else:
            identificacion = input("Ingrese un número de identificación válido, debe ser solo numerico: ")

# valida si el dato es vacio
def validarVacio(dato):
    while True:
        if dato != '':
            return dato
        else:
            dato = str(input("Ingrese un dato válido, no puede estar vacío: "))