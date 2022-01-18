package main

import "fmt"

func main() {
	var T int
	fmt.Scanln(&T)
	var inp int
	for i := 0; i < T; i++ {
		fmt.Scanln(&inp)
		fmt.Println("1", inp)
	}
}
