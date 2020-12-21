package main

import (
	"fmt"
	"math"
)

func main() {
	var testCases int
	fmt.Scanf("%d", &testCases)
	for i := 0; i < testCases; i++ {
		var N, V1, V2 int
		fmt.Scanf("%d %d %d", &N, &V1, &V2)
		stairTime := (math.Sqrt(float64(2)) * float64(N)) / float64(V1)
		elevatorTime := (float64(N) * float64(2)) / float64(V2)
		if stairTime > float64(elevatorTime) {
			fmt.Println("Elevator")
		} else {
			fmt.Println("Stairs")
		}
	}
}
