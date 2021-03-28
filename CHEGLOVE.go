package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func sliceconvAtoI(strarr []string) ([]int, error) {
	si := make([]int, 0, len(strarr))
	for _, a := range strarr {
		i, err := strconv.Atoi(a)
		if err != nil {
			return si, err
		}
		si = append(si, i)
	}
	return si, nil
}
func main() {
	var testCases, fingers int
	var fingerLength []int
	var front, back bool
	var gloveLength []int
	fmt.Scanf("%d", &testCases)
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; i < testCases; i++ {
		fmt.Scanf("%d", &fingers)
		scanner.Scan()
		line := scanner.Text()
		lineArr := strings.Fields(line)
		fingerLength, _ = sliceconvAtoI(lineArr)
		scanner.Scan()
		line = scanner.Text()
		lineArr = strings.Fields(line)
		gloveLength, _ = sliceconvAtoI(lineArr)
		//		fmt.Println(len(fingerLength), fingerLength)
		//		fmt.Println(len(gloveLength), gloveLength)

		for i := 1; i <= fingers; i++ {
			if fingerLength[i-1] > gloveLength[i-1] {
				front = false
				break
			} else {
				front = true
			}
		}
		for i, j := 0, fingers-1; i < fingers; i++ {
			if fingerLength[i] > gloveLength[j] {
				back = false
				break
			} else {
				back = true
			}
			j--
		}
		if front && back {
			fmt.Println("both")
		} else if front {
			fmt.Println("front")
		} else if back {
			fmt.Println("back")
		} else {
			fmt.Println("none")
		}

	}
}
