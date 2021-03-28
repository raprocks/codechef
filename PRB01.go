package main

import (
	"fmt"
	"math"
)

func primeTest(n int) bool {
	if n == 1 {
		return false
	} else if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	sqrt := math.Floor(math.Sqrt(float64(n)))
	for i := 3; i < int(sqrt); i = i + 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}
func main() {
	var testCases, num int
	var res bool
	fmt.Scanf("%d", &testCases)
	for i := 0; i < testCases; i++ {
		fmt.Scanf("%d", &num)
		res = primeTest(num)
		if res {
			fmt.Println("yes")
		} else {
			fmt.Println("no")
		}
	}
}
