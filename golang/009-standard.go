package main

import "fmt"

func main() {
	for a := 1; a <= 1000; a++ {
		for b := 1; a+b <= 1000; b++ {
			if c := 1000 - a - b; a*a+b*b == c*c {
				fmt.Println(a * b * c)
				return
			}
		}
	}
}
