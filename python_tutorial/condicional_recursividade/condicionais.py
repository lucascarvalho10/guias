# A keyword pass, quando em funções ou condicionais, não faz nada
if True:
    pass

x = 10

# È possível encadear os "ifs"
if x == 2:
    print("Vale dois")
elif x == 5:
    print("Vale cinco")
else:
    print("Vale outra coisa")

# Isto é bem legal!
if 0 < x <= 10:
    print('Essa sintaxe e util e inteligente!')
