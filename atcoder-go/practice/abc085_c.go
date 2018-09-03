package main

import (
	"fmt"
)

func main() {
	var n, y int
	fmt.Scan(&n, &y)
	i := -1
	j := -1
	k := -1
	for i = 0; i <= n; i++ {
		m := n - i
		x := y - i*10000
		z := x - 1000*m
		if z >= 0 && z%4000 == 0 {
			j = z / 4000
			k = m - j
			if k >= 0 {
				break
			}
		}
	}
	if j < 0 || k < 0 {
		i, j, k = -1, -1, -1
	}
	fmt.Print(i, j, k)
}
