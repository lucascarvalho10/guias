#include <stdio.h>

/* Definindo uma macros.

Essa função está pronta em tempo de compilação.

Além disso, não há restrição do tipo de dado na chamada */
#define max(a, b) ((a > b) ? a : b)

#define swap(a, b) {a = a * b;  b = a/b; a = a/b;}


int main (void) {
    int a = 2, b =10;

    printf("%d ", max(a, b));
    swap(a, b);
    printf("%d %d", a, b);
    return 0;
}