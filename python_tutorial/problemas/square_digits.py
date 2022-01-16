def square_digits(num):
    return int(''.join([str(n**2) for n in map(int, list(str(num)))]))


print(square_digits(9119))
