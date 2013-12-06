package main

import "fmt"

func worker(inbox, outbox chan int) {
	for a := range inbox {
		for b := 1; a+b <= 1000; b++ {
			if c := 1000 - a - b; a*a+b*b == c*c {
				outbox <- a * b * c
			}
		}
	}
}

func main() {
	ans := make(chan int)
	jobs := make(chan int)
	for i := 0; i < 8; i++ {
		go worker(jobs, ans)
	}

	go func() {
		for a := 1; a <= 1000; a++ {
			jobs <- a
		}
	}()
	fmt.Println(<-ans)
}
