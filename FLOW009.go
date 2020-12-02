package main

import (
	"fmt"
	"strconv"
)

func main() {
	var testCases int
	var inp, inp2 string
	fmt.Scanln(&testCases)

	for i := 0; i < testCases; i++ {
		fmt.Scanln(&inp, &inp2)
		quantity, _ := strconv.Atoi(inp)
		price, _ := strconv.ParseFloat(inp2, 64)
		if quantity > 1000 {
			price = price - (0.1 * price)
		}
		fmt.Printf("%.6f\n", float64(price*float64(quantity)))
	}
}
