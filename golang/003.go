package main

import "fmt"

import "./euler"

func main() {
    num := 600851475143
    for !euler.IsPrime(num) {
        primes := euler.MakePrimeChannel()
        for prime := range primes {
            if num%prime == 0 {
                num /= prime
                break
            }
        }
    }
	fmt.Println(num)
}
