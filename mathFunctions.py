import math

def potencia(a, b):
    '''Calcula a potencia b de um numro a'''
    return a ** b

def raiz(a, b):
    '''Calcula a raiz b-gesima potencia de a'''
    return math.sqrt(a,b)

def circuferencia(raio):
    '''Calcula a circuferencia de um circulo'''
    return 2 * raio * math.PI

def areaCirculo(raio):
    '''Calcula a area de um circulo'''
    return math.PI * raio ** 2

def volumeCubo(aresta):
    '''Calcula o volume de um Cubo'''
    return aresta ** 3

def volumePiramide(aresta, altura):
    '''Calcula o volume de uma piramide'''
    base = aresta ** 2
    return (base * altura)/3

def areaCilindro(raio, altura):
    '''Calcula a area de um cilindro'''
    areaBases = 2 * math.PI * raio ** 2
    areaLateral = 2 * math.PI * raio * altura
    return areaBases + areaLateral

def volumeCilindro(raio, altura):
    '''Calcula o volume de um cilindro'''
    areaBase = math.PI * raio ** 2
    return areaBase * altura

def volumeCone(raio, altura):
    '''Calcula o volume de um cone'''
    areaBase = math.PI * raio ** 2
    return (areaBase * altura)/3

