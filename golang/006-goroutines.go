package main

import "fmt"

func main() {
	sumsquares, squaresum := make(chan int), make(chan int)
	go func() {
		var n int
		for i := 0; i <= 100; i++ {
			n += i * i
		}
		sumsquares <- n
	}()
	go func() {
		var n int
		for i := 0; i <= 100; i++ {
			n += i
		}
		squaresum <- n * n
	}()
	fmt.Println(<-squaresum - <-sumsquares)
}
