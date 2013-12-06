package main

import "fmt"

import "./euler"

func main() {
	num := 600851475143
	for !euler.IsPrime(num) {
		for prime := range euler.Primes() {
			if num%prime == 0 {
				num /= prime
				break
			}
		}
	}
	fmt.Println(num)
}
