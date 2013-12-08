package main

import "fmt"

var wordLengths = map[int]int{
	0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
	11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6,
	30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8,
}

func numToLength(n int) int {
	if n == 1000 {
		return wordLengths[1] + wordLengths[1000]
	} else if n%100 == 0 {
		return wordLengths[n/100] + wordLengths[100]
	} else if n > 100 {
		return numToLength(n-n%100) + 3 + numToLength(n%100) // the word "and"
	} else if n > 10 && n < 20 {
		return wordLengths[n]
	} else {
		return wordLengths[n-n%10] + wordLengths[n%10]
	}
}

func main() {
	ans := 0
	for i := 1; i <= 1000; i++ {
		ans += numToLength(i)
	}
	fmt.Println(ans)
}
