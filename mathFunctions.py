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



