package main

import "fmt"

func main() {
	var T, x, m, d int
	fmt.Scanln(&T)
	for i := 0; i < T; i++ {
		fmt.Scanf("%d %d %d\n", &x, &m, &d)
		delayed := x * m
		if delayed > x+d {
			delayed = x + d
		}
		fmt.Println(delayed)
	}

}
