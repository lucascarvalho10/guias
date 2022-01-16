#include <stdio.h>

/* Printar um valor em decimal, imprimiremos uma string */
void printd(int);

int main (void) {
    printd(-1390);

    return 0;
}

void printd (int n) {
    /* Se ele escreve um valor negativo, apenas adicionamos um sinal de menos */
    if (n < 0) {
        putchar('-');
        n = -n;
    }

    if (n/10) printd(n/10);
    putchar(n%10 + '0');
}