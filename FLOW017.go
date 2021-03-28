package main

import (
	"fmt"
)

func main() {
	var testCases int
	fmt.Scanf("%d", &testCases)
	for i := 0; i < testCases; i++ {
		var A, B, C int
		fmt.Scanf("%d %d %d", &A, &B, &C)
		var max, min int
		if A < B {
			max = B
			min = A
		} else {
			max = A
			min = B
		}
		if max > C {
			if min <= C {
				fmt.Println(C)
			} else {
				fmt.Println(min)
			}
		} else {
			fmt.Println(max)
		}
	}
}
