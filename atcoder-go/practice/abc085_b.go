package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	d := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&d[i])
	}
	sort.Ints(d)
	result := 0
	p := -1
	for i := n - 1; i >= 0; i-- {
		if d[i] != p {
			result++
		}
		p = d[i]
	}
	fmt.Print(result)
}
