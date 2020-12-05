package main

import (
	"fmt"
)

func main() {
	var testCases, hardness, tensileStrength int
	var carbonContent float64
	fmt.Scanln(&testCases)
	for i := 0; i < testCases; i++ {
		fmt.Scanf("%d %f %d", &hardness, &carbonContent, &tensileStrength)
		score := 0
		if hardness > 50 {
			score++
		}
		if carbonContent < 0.7 {
			score += 2
		}
		if tensileStrength > 5600 {
			score += 4
		}
		switch score {
		case 0:
			fmt.Println("5")
		case 1:
			fmt.Println("6")
		case 2:
			fmt.Println("6")
		case 3:
			fmt.Println("9")
		case 4:
			fmt.Println("6")
		case 5:
			fmt.Println("7")
		case 6:
			fmt.Println("8")
		case 7:
			fmt.Println("10")
		}

	}
}
