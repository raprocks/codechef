package main

import "fmt"

func main() {
	var N int

	fmt.Scanln(&N)

	if N%5 == 0 && N%11 == 0 {
		fmt.Println("BOTH")
	} else if N%5 == 0 || N%11 == 0 {
		fmt.Println("ONE")
	} else {
		fmt.Println("NONE")
	}
}
