package main

import "fmt"

func main() {
	var ans int
	for i := 0; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			ans += i
		}
	}
	fmt.Println(ans)
}
