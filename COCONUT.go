package main

import (
	"fmt"
	"math"
)

func main() {
	var T int
	var (
		xa, xb, Xa, Xb int
	)
	fmt.Scanln(&T)

	for i := 0; i < T; i++ {
		fmt.Scanln(&xa, &xb, &Xa, &Xb)
		reqa := math.Ceil(float64(Xa) / float64(xa))
		reqb := math.Ceil(float64(Xb) / float64(xb))
		fmt.Println(int(reqa) + int(reqb))
	}
}
