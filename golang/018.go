package main

import "fmt"
import "strconv"
import "strings"

var triangle [15][15]int
var cost [15][15]int

var rawData = `75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23`

func main() {
	for lineNo, line := range strings.Split(rawData, "\n") {
		for valueNo, valueStr := range strings.Split(line, " ") {
			value, err := strconv.Atoi(valueStr)
			if err != nil {
				fmt.Println("Found error at line", lineNo, "position", valueNo)
				fmt.Println(err)
				return
			}
			triangle[lineNo][valueNo] = value
		}
	}

	cost[0][0] = triangle[0][0]
	for row := 0; row < len(triangle)-1; row++ {
		for col := 0; col <= row; col++ {
			if newCost := cost[row][col] + triangle[row+1][col]; cost[row+1][col] < newCost {
				cost[row+1][col] = newCost
			}
			if newCost := cost[row][col] + triangle[row+1][col+1]; cost[row+1][col+1] < newCost {
				cost[row+1][col+1] = newCost
			}
		}
	}

	ans := 0
	for i := 0; i < len(cost[len(cost)-1]); i++ {
		if cost[len(cost)-1][i] > ans {
			ans = cost[len(cost)-1][i]
		}
	}
	fmt.Println(ans)
}
