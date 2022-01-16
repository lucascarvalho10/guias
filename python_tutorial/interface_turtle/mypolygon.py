# A biblioteca turtle permite criar imagens
import turtle

lucas = turtle.Turtle()
print(lucas)

# rt: virar à direita
# lt: virar à esquerda
# bk: para trás
# fd: para frente

for _ in range(4):
    lucas.fd(100)
    lucas.lt(90)


turtle.mainloop()
