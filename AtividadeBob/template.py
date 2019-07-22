import math

def desenhar(t, comp):
        t.penup()
        t.fd(comp + 10)
        t.pendown()


def linha(t, n_lado, comprimento, angulo):
        for i in range(n_lado):
                t.fd(comprimento)
                t.lt(angulo)


def quadrado(t, comprimento):
        for i in range(4):
                t.fd(comprimento)
                t.lt(90)


def poligono(t, n_lado,comprimento):
        angulo = 360 / n_lado
        linha(t, n_lado, comprimento, angulo)


def circulo (t, raio):
        arco(t, raio, 360)


def arco (t, raio, angulo):
        circunferencia = 2 * math.pi * raio
        n_lado = 60
        comprimento_arco = circunferencia / n_lado
        angulo_arco = angulo / n_lado
        linha(t, n_lado, comprimento_arco, angulo_arco)

        