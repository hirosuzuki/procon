package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	sort.Ints(a)
	var alice, bob int
	for i := n - 1; i >= 0; i -= 2 {
		alice += a[i]
	}
	for i := n - 2; i >= 0; i -= 2 {
		bob += a[i]
	}
	fmt.Print(alice - bob)
}
