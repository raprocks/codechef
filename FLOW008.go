package main

import (
	"fmt"
)

func main() {
	var testCases int
	var scannedInt int
	fmt.Scanln(&testCases)
	for i := 0; i < testCases; i++ {
		fmt.Scanln(&scannedInt)
		if scannedInt < 10 {
			fmt.Println("Thanks for helping Chef!")
		} else {
			fmt.Println("-1")
		}
	}
}
