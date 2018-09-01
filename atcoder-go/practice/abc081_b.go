package main

import (
	"fmt"
)

func calc_bin(n int) (result int) {
	if n <= 0 {
		return
	}
	for n&1 == 0 {
		result++
		n >>= 1
	}
	return
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	result := 100000000000000000
	for _, x := range a {
		result = min(result, calc_bin(x))
	}
	fmt.Print(result)
}
