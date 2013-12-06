package main

import "fmt"

import "./util"

// NUM := 600851475143
var NUM int = 1e7

func main() {
    var ans int
    primes := util.LimitIntChannel(util.MakePrimeChannel(), NUM+1)
    for potentialPrimeFactor := range primes {
        ans = potentialPrimeFactor
        fmt.Println(ans)
    }
    fmt.Println(ans)
}
