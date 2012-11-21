#include <stdio.h>

int lcm(int, int);
int gcd(int, int);

int main() {
    int ans = 1;

    for (int i = 2; i <= 20; i++) {
        ans = lcm(ans, i);
    }

    printf("%d\n", ans);
    return 0;
}

// we don't have to worry about
// negative values of a and b here
int lcm(int a, int b) {
    return a / gcd(a, b) * b;  // prevent overflow
}

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}
