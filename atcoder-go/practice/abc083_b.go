package main

import (
	"fmt"
)

func calc_digits(x int) (result int) {
	for x > 0 {
		result += x % 10
		x /= 10
	}
	return
}

func main() {
	var n, a, b int
	fmt.Scan(&n, &a, &b)
	result := 0
	for i := 1; i < n+1; i++ {
		r := calc_digits(i)
		if r >= a && r <= b {
			result += i
		}
	}
	fmt.Print(result)
}
