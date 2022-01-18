package main

import (
	"fmt"
)

func remove(x []int, y int) []int {
	var idx int
	var out []int
	for i := 0; i < len(x); i++ {
		if x[i] == y {
			idx = i
			break
		}
	}
	for i := 0; i < len(x); i++ {
		if i == idx {
			continue
		}
		out = append(out, x[i])
	}
	return out
}
func max(x []int) int {
	curmax := x[0]
	for _, v := range x {
		if v > curmax {
			curmax = v
		}
	}
	return curmax
}
func sum(x []int) int {
	total := 0
	for _, v := range x {
		total += v
	}
	return total
}
func main() {
	var T, D, E int
	var possible bool
	fmt.Scanln(&T)
	for i := 0; i < T; i++ {
		var bags_array [3]int

		for i := 0; i < 3; i++ {
			fmt.Scanf("%d", &bags_array[i])
		}
		fmt.Scanln(&D, &E)
		var bags = bags_array[0:len(bags_array)]
		possible = (sum(bags) <= (D + E))
		if !(possible) {
			fmt.Println("NO")
			continue
		}
		var carrieable_candidates []int
		for i := 0; i < 3; i++ {
			if bags[i] <= E {
				carrieable_candidates = append(carrieable_candidates, bags[i])
			}
		}
		if len(carrieable_candidates) == 0 {
			fmt.Println("NO")
			continue
		}
		var max_carriable = max(carrieable_candidates)
		bags = remove(bags, max_carriable)
		if sum(bags) <= D {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
}
