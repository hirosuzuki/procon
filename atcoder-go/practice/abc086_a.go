package main

import (
	"fmt"
)

func main() {
	var a, b int64
	fmt.Scanf("%d %d\n", &a, &b)
	if a*b%2 == 0 {
		fmt.Println("Even")
	} else {
		fmt.Println("Odd")
	}
}
