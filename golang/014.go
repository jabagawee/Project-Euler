package main

import "fmt"

func makeMemoizedCollatzLength() func(int)int {
    memo := make(map[int]int)
    memo[1] = 1

    var collatzLength func(int)int
    collatzLength = func (n int) int {
        if memo[n] != 0 {
            return memo[n]
        }

        if n%2 == 0 {
            memo[n] = 1 + collatzLength(n/2)
        } else {
            memo[n] = 1 + collatzLength(3*n+1)
        }
        return memo[n]
    }
    return collatzLength
}

func main() {
    var ans, maxLength int
    collatzLength := makeMemoizedCollatzLength()
    collatzLengths := make(chan int)
    go func() {
        for i := 1; ; i++ {
            collatzLengths <- collatzLength(i)
        }
    }()
    for i := 1; i <= 1000000; i++ {
        if length := <-collatzLengths; length > maxLength {
            maxLength = length
            ans = i
        }
    }
    fmt.Println(ans)
}
