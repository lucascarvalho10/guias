import time

# Como é intuitivo, time() retorna o total de segundos passados desde uma semente qualquer
tempo = time.time()
hora = tempo//3600
dia = tempo//86400
mes = tempo//2600000
ano = tempo//31500000

print(ano, mes, dia, hora)


def is_triangle(a, b, c):
    """Verifica a desigualdade triangular, não valem valores negativos"""
    return "Yes" if (a < b + c and b < a + c and c < a + b) else "No"


print(is_triangle(3, 4, 5))
