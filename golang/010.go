package main

import "fmt"

import "./euler"

func main() {
	var ans int
	primes := euler.Primes()
	smallPrimes := euler.CapIntChannel(primes, 2000000)
	for prime := range smallPrimes {
		ans += prime
	}
	fmt.Println(ans)
}
