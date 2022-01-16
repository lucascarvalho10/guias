#include <stdio.h>

/* Declarar algo como estático esconde ela de outros possíveis arquivos */
static int num;

static int conta (int *num, int qtd) {
    int i;
    for (i = 0; i < qtd; i++) printf("%d", *(num + i));
}

int main (void) {
    /* Caso a declaração seja interna a uma função, elas permanecem, não 
    sendo afetadas com o vai e vem das chamadas.
    
    Em suma, garantem salvamente permanente*/
    static int valor;


    /* Sinaliza o compilador que se trata de uma variável massivamente usada.
    Assim, ela, preferencialmente, deve ser alocada em um registrador */
    register double conta;

    char palavra [4] = {'o', 'l', 'a', '\0'};

    printf("%s", palavra);

    return 0;
}
