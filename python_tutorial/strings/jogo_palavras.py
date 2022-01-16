fin = open("palavras.txt")


# def mais_vinte(fin):
#     for linha in fin:
#         palavra = linha.strip()
#         if (len(palavra) > 20):
#             print(palavra)


def nao_e(fin):
    for linha in fin:
        palavra = linha.strip()
        if ('e' not in palavra):
            print(palavra)


nao_e(fin)
