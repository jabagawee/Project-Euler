package main

import "fmt"

func abs(n int) int {
	if n < 0 {
		return -n
	} else {
		return n
	}
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	} else {
		return gcd(b, a%b)
	}
}

func lcm(a, b int) int {
	return abs(a*b) / gcd(a, b)
}

func main() {
	ans := 1
	for i := 1; i <= 20; i++ {
		ans = lcm(ans, i)
	}
	fmt.Println(ans)
}
