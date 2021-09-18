package main

import (
	"fmt"
)

func main() {
	var T, D, E int
	fmt.Scanln(&T)
	for i := 0; i < T; i++ {
		var a [3]int
		for i := 0; i < 3; i++ {
			fmt.Scanf("%d", &a[i])
		}
		fmt.Scanln(&D, &E)
		if a[0] <= E {
			if a[1]+a[2] <= D {
				fmt.Println("YES")
			} else {
				fmt.Println("NO")
			}
		} else if a[1] <= E {
			if a[0]+a[2] <= D {
				fmt.Println("YES")
			} else {
				print("internal\n")
				fmt.Println("NO")
			}
		} else if a[2] <= E {
			if a[1]+a[0] <= D {
				fmt.Println("YES")
			} else {
				fmt.Println("NO")
			}
		} else {
			fmt.Println("NO")
		}
	}
}
