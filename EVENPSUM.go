package main

import (
	"fmt"
)

func main() {
	var testCases, A, B, counter int
	fmt.Scanf("%d", &testCases)
	for i := 0; i < testCases; i++ {
		counter = 0
		fmt.Scanf("%d %d", &A, &B)
		for x := 1; x <= A; x++ {
			for y := 1; y <= B; y++ {
				//				fmt.Println("(", x, ",", y, ")")
				if (x+y)%2 == 0 {
					//					fmt.Println("increase counter")
					counter++
				}
			}
		}
		fmt.Println(counter)
	}
}
