import turtle

t = turtle.Turtle()


def koch(t, x):
    """Desenha o fractal de koch de tamanho x seguindo uma norma recursiva"""
    if x < 3:
        t.fd(x)
        return
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)
    t.rt(120)
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)


koch(t, 100)
turtle.mainloop()
