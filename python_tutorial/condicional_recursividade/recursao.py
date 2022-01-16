# Python permite implementar fuções recursivas

def fatorial(n):
    """Resolve o fatorial de n"""
    return 1 if (n == 0) else fatorial(n - 1)*n


print(fatorial(170))
