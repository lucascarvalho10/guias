# Expressão regular em um arquivo de texto


# Para rodar:  type texto.txt | python egrep.py "ola"
# Este é o caractere pipe |, que significa “use a saída do comando da esquerda

import sys  # O módulo sys fornece funções e variáveis ​​usadas para manipular diferentes partes do ambiente de tempo de execução do Python
import re  # Expressões regulares

# sys.argv é a lista dos argumentos da linha de comandos
# sys.argv [0] é o nome do programa em si
# sys.argv [1] será o regex especificado na linha de comandos
regex = sys.argv[1]
# para cada linha passada pelo script
for line in sys.stdin:
    # se combinar com o regex, escreva-o para o stdout
    if re.search(regex, line):
        sys.stdout.write(line)
