#define MAX(x, y) (((x) > (y)) ? (x) : (y))

#include <stdio.h>
#include <stdbool.h>

bool is_palindrome(int);

int main() {
    int ans = 0;
    int k;

    for (int i = 100; i < 1000; i++) {
        for (int j = 100; j < 1000; j++) {
            k = i * j;
            if (is_palindrome(k)) {
                ans = MAX(ans, k);
            }
        }
    }

    printf("%d\n", ans);
    return 0;
}

bool is_palindrome(int candidate) {
    int rev = 0;
    int n = candidate;

    while (n > 0) {
        rev *= 10;
        rev += n % 10;
        n /= 10;
    }

    return rev == candidate;
}
