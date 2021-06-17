package main

import "fmt"

func main() {
	var arr [3]int
	var largest, second_largest int

	for i := 0; i < 3; i++ {
		fmt.Println(&arr[i])
	}
	for _, element := range arr {
		if element > largest {
			largest = element
		} else if element < largest && element > second_largest {
			second_largest = element
		}
	}
	fmt.Println(second_largest)

}
