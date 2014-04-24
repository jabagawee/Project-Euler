package main

import "fmt"
import "time"

func main() {
	ans := 0
	for year := 1901; year <= 2000; year++ {
		for month := 1; month <= 12; month++ {
			date := time.Date(year, time.Month(month), 1, 12, 0, 0, 0, &time.Location{})
			if date.Weekday().String() == "Sunday" {
				ans++
			}
		}
	}
	fmt.Println(ans)
}
