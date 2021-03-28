package main

import (
	"fmt"
	"math"
)

func checkPrime(n int) bool {
	for i := 2; i < (int(math.Sqrt(float64(n))) + 1); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true

}

func main() {
	var testCases, x, y int
	fmt.Scanln(&testCases)
	for i := 0; i < testCases; i++ {
		fmt.Scanf("%d %d", &x, &y)
		sum := x + y
		addr := 1
		found := false
		for !found {
			localSum := sum + addr
			res := checkPrime(localSum)
			if res == true {
				found = true
				fmt.Println(addr)
			} else {
				addr++
			}
		}
	}
}
