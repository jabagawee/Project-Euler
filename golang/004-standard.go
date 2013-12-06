package main

import "fmt"

func isPalindrome(n int) bool {
	n1, n2 := n, 0
	for n != 0 {
		n2 *= 10
		n2 += n % 10
		n /= 10
	}
	return n1 == n2
}

func main() {
	var ans int
	for i := 900; i < 1000; i++ {
		for j := 900; j < 1000; j++ {
			k := i * j
			if isPalindrome(k) && k > ans {
				ans = k
			}
		}
	}
	fmt.Println(ans)
}
