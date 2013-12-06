package main

import "fmt"

func main() {
	var sumsquares, squaresum int
	for i := 0; i <= 100; i++ {
		sumsquares += i * i
		squaresum += i
	}
	squaresum *= squaresum
	fmt.Println(squaresum - sumsquares)
}
