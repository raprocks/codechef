package main

import "fmt"

func max(x []int) int {
	curmax := x[0]
	curmaxIdx := 0
	for i, v := range x {
		if v > curmax {
			curmaxIdx = i
		}
	}
	return curmaxIdx
}

func min(x []int) int {
	curmin := x[0]
	curminIdx := 0
	for i, v := range x {
		if v < curmin {
			curminIdx = i
		}
	}
	return curminIdx
}
func swap(x []int, y []int, a int, b int) {
	x[a], y[b] = y[b], x[a]
}
func sum(x []int) int {
	total := 0
	for _, v := range x {
		total += v
	}
	return total
}
func main() {
	var testCases int
	fmt.Scanf("%d\n", &testCases)
	for i := 0; i < testCases; i++ {
		var N, M int
		fmt.Scanf("%d %d\n", &N, &M)
		A := make([]int, N)
		for i := range A {
			fmt.Scanf("%d", &A[i])
		}
		fmt.Scanf("\n")
		B := make([]int, M)
		for i := range B {
			fmt.Scanf("%d", &B[i])
		}
		fmt.Scanf("\n")
		var counter int
		sumA := sum(A)
		sumB := sum(B)
		maxLimit := N * M
		for sumA <= sumB {
			counter++
			swap(A, B, min(A), max(B))
			sumA = sum(A)
			sumB = sum(B)
			if counter > maxLimit {
				break
			}
		}
		if sumA > sumB {
			fmt.Println(counter)
		} else {
			fmt.Println(-1)
		}
	}
}
