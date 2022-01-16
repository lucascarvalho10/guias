import turtle


def square(t, l):
    """Função que desenha um quadrado de lado l a partir do objeto t"""
    for _ in range(4):
        t.fd(l)
        t.lt(90)
    turtle.mainloop()


poligono = turtle.Turtle()
# square(quad, 300)

# Desenhando um polígono regular qualquer
# ângulos internos: 360/n


def polygon(t, n, l):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle. Chamamos isso de docstring
    """
    for _ in range(n):
        t.fd(l)
        t.lt(360/n)
    turtle.mainloop()


polygon(poligono, 100, 10)
