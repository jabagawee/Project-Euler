package main

import "fmt"
import "io/ioutil"
import "strconv"
import "strings"

var triangle [100][100]int
var cost [100][100]int

func main() {
    rawByteData, err := ioutil.ReadFile("triangle.txt")
    if err != nil {
        fmt.Println(err)
        return
    }
    rawData := string(rawByteData)
	for lineNo, line := range strings.Split(strings.TrimSpace(rawData), "\n") {
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
