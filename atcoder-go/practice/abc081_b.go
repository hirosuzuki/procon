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

func arrayMap(xs []int, f func(int) int) []int {
	result := make([]int, len(xs))
	for i := 0; i < len(xs); i++ {
		result[i] = f(xs[i])
	}
	return result
}

func min(xs []int) int {
	result := xs[0]
	for _, r := range xs[1:] {
		if r < result {
			result = r
		}
	}
	return result
}

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	b := arrayMap(a, calc_bin)
	result := min(b)
	fmt.Print(result)
}
