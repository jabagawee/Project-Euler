#include <stdio.h>
#include <stdlib.h>

int sum_square_digits(int num) {
    int ret = 0;
    while (num > 0) {
        ret += (num%10) * (num%10);
        num /= 10;
    }
    return ret;
}

int main() {
    int ans = 0;
    int *cache;
    cache = malloc (sizeof(int) * 10000003);
    for (int i = 0; i < 10000003; i++) {
        cache[i] = 0;
    }
    cache[1] = 1;
    cache[89] = 89;

    int temp;

    for (int i = 2; i <= 10000000; i++) {
        temp = i;
        while (cache[temp] == 0) {
            temp = sum_square_digits(temp);
        }
        cache[i] = cache[temp];
        if (cache[i] == 89) {
            ans++;
        }
    }

    printf("%d\n", ans);
    return 0;
}
