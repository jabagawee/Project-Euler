package main

import "fmt"
import "math/big"
import "strconv"

func main() {
	hugeNum := new(big.Int)
	hugeNum.Exp(big.NewInt(2), big.NewInt(1000), nil)
	ans := 0

	for _, digitChar := range hugeNum.String() {
		digit, err := strconv.Atoi(string(digitChar))
		if err != nil {
			fmt.Println("Well that shouldn't have happened...")
			fmt.Println("Got error:", err)
			return
		}
		ans += digit
	}

	fmt.Println(ans)
}
