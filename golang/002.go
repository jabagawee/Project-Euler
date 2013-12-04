package main

import "fmt"

func isEven(n int) bool {
	return n%2 == 0
}

func main() {
	var ans int
	fib := makeFibonacciChannel()
	evenFib := filterIntChannel(isEven, fib)
	evenSmallFib := limitIntChannel(evenFib, 4000000+1)
	for i := range evenSmallFib {
		ans += i
	}
	fmt.Println(ans)
}
