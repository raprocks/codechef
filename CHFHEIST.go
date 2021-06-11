package main

import (
	"fmt"
)

func main() {
	var T, D, d, P, Q, partialhold, lefthold, totalparts, leftdays int
	fmt.Scanf("%d\n", &T)
	for i := 0; i < T; i++ {
		fmt.Scanf("%d %d %d %d\n", &D, &d, &P, &Q)
		totalparts = D / d
		// fmt.Println("totalparts", totalparts)
		leftdays = D % d
		//fmt.Println("leftdays", leftdays)
		partialhold = d * totalparts * (2*P + (totalparts-1)*Q)
		partialhold = partialhold / 2
		lefthold = leftdays * (P + totalparts*Q)
		//fmt.Println("partialhold", partialhold, "lefthold", lefthold)
		fmt.Println(partialhold + lefthold)
	}
}
