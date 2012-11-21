#include <math.h>
#include <stdio.h>
#include <stdbool.h>

bool is_prime(long long);
long long remove_lowest_prime(long long);

int main() {
    long long num = 600851475143;

    while (!is_prime(num)) {
        num = remove_lowest_prime(num);
    }

    printf("%lld\n", num);
    return 0;
}

bool is_prime(long long candidate) {
    for (long long i = 2; i < ceil(sqrt(candidate)); i++) {
        if (candidate % i == 0) {
            return false;
        }
    }
    return true;
}

long long remove_lowest_prime(long long composite) {
    for (long long i = 2; i < ceil(sqrt(composite)); i++) {
        if (composite % i == 0) {
            return composite / i;
        }
    }
}
