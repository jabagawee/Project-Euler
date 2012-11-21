#define INV_SQRT5 0.4472135954
#define PHI 1.6180339887

#include <math.h>
#include <stdio.h>

int fibonacci(int);

int main() {
    int ans = 0;
    int i = 0;
    int f = fibonacci(i);

    while (f < 4000000) {
        if (f % 2 == 0) {
            ans += f;
        }
        i++;
        f = fibonacci(i);
    }

    printf("%d\n", ans);
    return 0;
}

int fibonacci(int n) {
    return (int) (pow(PHI, n) * INV_SQRT5 + 0.5);
}
