package main

import "fmt"

import "./euler"

func numFactors(n int) int {
    numFactors := 1
    for _, cardinality := range euler.PrimeFactorize(n) {
        numFactors *= cardinality + 1
    }
    return numFactors
}

func main() {
    for triangle := range euler.Triangles() {
        if numFactors(triangle) > 500 {
            fmt.Println(triangle)
            return
        }
    }
}
