package main

import (
	"fmt"
)

func main() {
	var testCases int
	fmt.Scanf("%d", &testCases)
	for i := 0; i < testCases; i++ {
		var N int
		fmt.Scanf("%d", &N)
		matrix := make([][]int, N)
		for i := 0; i < N; i++ {
			row := make([]int, N)
			for j := 0; j < N; j++ {
				fmt.Scanf("%d", &row[j])
			}
			matrix[i] = row
		}
		//		fmt.Println()
		//		fmt.Println()
		sumArr := make([]int, (2*N)-1)
		sumIdx := 0
		sum := 0
		for j := N - 1; j >= 0; j-- {
			i := 0
			//			fmt.Println()
			sum = 0
			for k := j; k < N; k++ {
				//				fmt.Println(i, k)
				sum += matrix[i][k]
				i++
			}
			sumArr[sumIdx] = sum
			sumIdx++
		}
		for i := N - 1; i > 0; i-- {
			j := 0
			//			fmt.Println()
			sum = 0
			for k := i; k < N; k++ {
				//				fmt.Println(k, j)
				sum += matrix[k][j]
				j++
			}
			sumArr[sumIdx] = sum
			sumIdx++
		}
		max := 0
		for _, v := range sumArr {
			if v > max {
				max = v
			}
		}
		fmt.Println(max)
	}
}
