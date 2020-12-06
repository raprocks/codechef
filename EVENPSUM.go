package main

import (
	"fmt"
)

func findOdd(n int) (odd int) {
	var isNOdd bool
	if n%2 == 0 {
		isNOdd = false
	} else {
		isNOdd = true
	}
	if isNOdd == true {
		odd = n/2 + 1
	} else {
		odd = n / 2
	}
	return odd
}
func main() {
	var testCases, A, B, counter int
	fmt.Scanf("%d", &testCases)
	for i := 0; i < testCases; i++ {
		counter = 0
		fmt.Scanf("%d %d", &A, &B)
		oddA := findOdd(A)
		oddB := findOdd(B)
		evenA := A - oddA
		evenB := B - oddB
		counter = (oddA * oddB) + (evenA * evenB)

		fmt.Println(counter)
	}
}
