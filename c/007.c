#include <stdio.h>

// bitset code from comp.lang.c
#include <limits.h>  // for CHAR_BIT
#include <string.h>  // for memset()

#define BITMASK(b) (1 << ((b) % CHAR_BIT))
#define BITSLOT(b) ((b) / CHAR_BIT)
#define BITSET(a, b) ((a)[BITSLOT(b)] |= BITMASK(b))
#define BITCLEAR(a, b) ((a)[BITSLOT(b)] &= ~BITMASK(b))
#define BITTEST(a, b) ((a)[BITSLOT(b)] & BITMASK(b))
#define BITNSLOTS(nb) ((nb + CHAR_BIT - 1) / CHAR_BIT)
// solution to 10001 = x / ln x
#define NUM 116671

int main() {
    int counter = 0;
    char bitarray[BITNSLOTS(NUM)];
    memset(bitarray, 0, BITNSLOTS(NUM));

    for(int i = 2; i < NUM; i++) {
        if(!BITTEST(bitarray, i)) {
            if (counter++ == 10000) {
                printf("%d\n", i);
            }
            for(int j = i + i; j < NUM; j += i)
                BITSET(bitarray, j);
        }
    }

    return 0;
}
