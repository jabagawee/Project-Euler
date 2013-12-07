package main

import "fmt"

import "./euler"

func numFactors(n int) int {
	numFactors := 1
	for _, cardinality := range euler.PrimeFactorize(n) {
		numFactors *= cardinality + 1
	}
	return numFactors
}

func worker(inbox, outbox chan int) {
	for triangle := range inbox {
		if numFactors(triangle) > 500 {
			outbox <- triangle
			return
		}
	}
}

func main() {
	ans := 1 << 30
	possibleAnswers := make(chan int)
	jobs := euler.Triangles()
	for i := 0; i < 4; i++ {
		go worker(jobs, possibleAnswers)
	}

	for i := 0; i < 1; i++ {
		if possibleAnswer := <-possibleAnswers; possibleAnswer < ans {
			ans = possibleAnswer
		}
	}

	fmt.Println(ans)
}
