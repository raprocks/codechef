package main

import "fmt"

func main() {
	var N, count int
	var facts []int

	fmt.Scanln(&N)

	for i := 1; i < N+1; i++ {
		if N%i == 0 {
			count++
			facts = append(facts, i)
		}
	}
	fmt.Println(count)
	for _, val := range facts {
		fmt.Printf("%d ", val)
	}
}
