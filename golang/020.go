package main

import "fmt"
import "math/big"
import "strconv"

func main() {
    hugeNum := big.NewInt(1)
    for i := 1; i <= 100; i++ {
        hugeNum.Mul(hugeNum, big.NewInt(int64(i)))
    }

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
