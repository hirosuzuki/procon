package main

import (
	"fmt"
)

func main() {
	var a, b, k int
	fmt.Scan(&a, &b, &k)
	for k > 0 {
		a, b, k = a/2, b+a/2, k-1
		if k <= 0 {
			break
		}
		a, b, k = a+b/2, b/2, k-1
	}
	fmt.Println(a, b)
}
