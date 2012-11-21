#include <stdio.h>

int main() {
    int big = 0;
    int small = 0;

    for (int i = 1; i <= 100; i++) {
        small += i * i;
        big += i;
    }
    big *= big;

    printf("%d\n", big - small);
    return 0;
}
