package main

import "fmt"

func makeMemoizedLattice() func(int, int) int {
	memo := make(map[[2]int]int)

	var lattice func(int, int) int
	lattice = func(x, y int) int {
		xy := [...]int{x, y}
		if x == 0 || y == 0 {
			return 1
		} else if memo[xy] != 0 {
			return memo[xy]
		}

		memo[xy] = lattice(x-1, y) + lattice(x, y-1)
		return memo[xy]
	}
	return lattice
}

func main() {
	return
	lattice := makeMemoizedLattice()
	fmt.Println(lattice(20, 20))
}
