import math

def potencia(a, b):
    return a ** b

def raiz(a, b):
    return math.sqrt(a,b)

def circuferencia(raio):
    return 2 * raio * math.PI

def areaCirculo(raio):
    return math.PI * raio ** 2

def volumeCubo(aresta):
    return aresta ** 3

def volumePiramide(aresta, altura):
    base = aresta ** 2
    return (base * altura)/3

def areaCilindro(raio, altura):
    areaBases = 2 * math.PI * raio ** 2
    areaLateral = 2 * math.PI * raio * altura
    return areaBases + areaLateral

def volumeCilindro(raio, altura):
    areaBase = math.PI * raio ** 2
    return areaBase * altura

def volumeCone(raio, altura):
    areaBase = math.PI * raio ** 2
    return (areaBase * altura)/3

