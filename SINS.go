package main

import "fmt"

func main() {
	var T int
	var A, B int
	fmt.Scanln(&T)
	for i := 0; i < T; i++ {
		fmt.Scanf("%d %d\n", &A, &B)
		for true {
			if A < B {
				B = B - A
			} else if B < A {
				A = A - B
			}
			if A == 0 || B == 0 || A == B {
				break
			}

		}
		println(A + B)
	}
}
