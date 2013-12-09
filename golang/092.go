package main

import "fmt"

func sum_square_digits(n int) int {
    ret := 0
    for n > 0 {
        ret += (n%10) * (n%10)
        n /= 10
    }
    return ret
}

func main() {
    ans := 0
    cache := [10000001]int{}
    cache[1] = 1
    cache[89] = 89

    for i := 2; i <= 10000000; i++ {
        temp := i
        for cache[temp] == 0 {
            temp = sum_square_digits(temp)
        }
        cache[i] = cache[temp]
        if cache[i] == 89 {
            ans++
        }
    }

    fmt.Println(ans)
}
