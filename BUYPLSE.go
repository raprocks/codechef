package main

import (
	"fmt"
)

func main() {
	var (
		a int
		b int
		x int
		y int
	)
	fmt.Scanln(&a, &b, &x, &y)

	fmt.Println(a*x + b*y)

}
