package main

import (
	"fmt"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func main() {
	var n, x int
	fmt.Scan(&n, &x)
	xs := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&xs[i])
	}
	result := abs(xs[0] - x)
	for i := 1; i < n; i++ {
		result = gcd(result, abs(xs[i]-x))
	}
	fmt.Print(result)
}
