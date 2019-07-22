import turtle
from template import quadrado, desenhar, circulo, poligono, arco

def main():
    bob = turtle.Turtle()
    bob.speed(10)
    
    # Exercicio 1
    quadrado(bob, 60)
    desenhar(bob, 100)
    circulo(bob, 30)
    desenhar(bob, 50)
    poligono(bob, 6, 35)
    desenhar(bob, 100)
    arco(bob, 30, 90)
    bob.reset()

    turtle.mainloop()


if __name__ == '__main__':
    main()

