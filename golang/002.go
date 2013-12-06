package main

import "fmt"

import "./util"

func isEven(n int) bool {
	return n%2 == 0
}

func main() {
	var ans int
	fib := util.MakeFibonacciChannel()
	evenFib := util.FilterIntChannel(isEven, fib)
	evenSmallFib := util.LimitIntChannel(evenFib, 4000000+1)
	for i := range evenSmallFib {
		ans += i
	}
	fmt.Println(ans)
}
