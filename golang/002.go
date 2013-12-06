package main

import "fmt"

import "./euler"

func isEven(n int) bool {
	return n%2 == 0
}

func main() {
	var ans int
	fib := euler.MakeFibonacciChannel()
	evenFib := euler.FilterIntChannel(isEven, fib)
	evenSmallFib := euler.CapIntChannel(evenFib, 4000000+1)
	for i := range evenSmallFib {
		ans += i
	}
	fmt.Println(ans)
}
