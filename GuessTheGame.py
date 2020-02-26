import random
import sys

MIN = 0
MAX = 1000

minimo = MIN
maximo = MAX

contador = 1


def pedir_numero(invitacion):
    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            print("Solo están autorizados los caracteres [0-9].",
                  file=sys.stderr)
        else:
            return entrada


def pedir_numero_limite(invitacion, minimo, maximo):
    while True:
        invitacion = "{} entre {} y {} incluidos:".format(invitacion, minimo,
                                                          maximo)
        entrada = pedir_numero(invitacion)
        if minimo <= entrada <= maximo:
            return entrada


def jugar_una_vez(numero, minimo, maximo, contador):
    victoria = False
    # print("El numero que buscas es", numero)
    # print("El numero que busca se encuentra entre", minimo, "y", maximo)
    intento = pedir_numero_limite("Introduzca el numero que crea que es", minimo, maximo)
    if intento > numero:
        contador += 1
        print("El numero es demasiado grande!")
        maximo = intento
    if intento < numero:
        print("El numero es demasiado pequeño!")
        contador += 1
        minimo = intento
    if intento == numero:
        print("Enhorabuena, has acertado!")
        print("Solo has necesitado", contador, "intentos!")
        victoria = True
    return victoria, minimo, maximo, contador


def jugar_una_partida(numero, minimo, maximo, contador):
    while True:
        victoria, minimo, maximo, contador = jugar_una_vez(numero, minimo, maximo, contador)
        if victoria:
            break

def decidir_limites():
    while True:
        minimo = pedir_numero("¿Cual es el limite inferior?")
        maximo = pedir_numero("¿Cual es el limite superior?")
        if maximo > minimo:
            return minimo, maximo


def jugar():
    minimo, maximo = decidir_limites()
    numero = random.randint(minimo, maximo)
    jugar_una_partida(numero, minimo, maximo, contador)


jugar()
