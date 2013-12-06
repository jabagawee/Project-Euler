// thanks dsal and Athiwat from #go-nuts for the amazing amount of help
// and patience they showed
package main

import (
	"fmt"
	"sync"
)

func isPalindrome(n int) bool {
	n1, n2 := n, 0
	for n != 0 {
		n2 *= 10
		n2 += n % 10
		n /= 10
	}
	return n1 == n2
}

func check(i, j int, c chan<- int) {
	k := i * j
	if isPalindrome(k) {
		c <- k
	}
}

func worker(wg *sync.WaitGroup, ch <-chan int, outch chan<- int) {
	defer wg.Done()
	for i := range ch {
		for j := 900; j < 1000; j++ {
			check(i, j, outch)
		}
	}
}

func feedTheBatch(ch chan<- int) {
	for i := 900; i < 1000; i++ {
		ch <- i
	}
	close(ch)
}

func waitAndClose(wg *sync.WaitGroup, ch chan int) {
	wg.Wait()
	close(ch)
}

func main() {
	var ans int
	wg := &sync.WaitGroup{}
	possibleAnswers := make(chan int)
	batchCh := make(chan int)
	for i := 0; i < 8; i++ { // however many workers make sense
		wg.Add(1)
		go worker(wg, batchCh, possibleAnswers)
	}

	go feedTheBatch(batchCh)
	go waitAndClose(wg, possibleAnswers)

	for possibleAnswer := range possibleAnswers {
		if possibleAnswer > ans {
			ans = possibleAnswer
		}
	}
	fmt.Println(ans)
}
