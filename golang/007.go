package main

import "fmt"

import "./euler"

func main() {
	var ans int
	primes := euler.Primes()
	for i := 0; i < 10001; i++ {
		ans = <-primes
	}
	fmt.Println(ans)
}
