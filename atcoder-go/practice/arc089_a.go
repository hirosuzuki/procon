package main

import (
	"fmt"
)

func abs(x int) int {
	if x > 0 {
		return x
	}
	return -x
}

func solve(n int, t, x, y []int) bool {
	st, sx, sy := 0, 0, 0
	for i := 0; i < n; i++ {
		dt, dxy := t[i]-st, abs(x[i]-sx)+abs(y[i]-sy)
		if dxy > dt || (dxy-dt)%2 != 0 {
			return false
		}
		st, sx, sy = t[i], x[i], y[i]
	}
	return true
}

func main() {
	var n int
	fmt.Scan(&n)
	t := make([]int, n)
	x := make([]int, n)
	y := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&t[i], &x[i], &y[i])
	}
	if solve(n, t, x, y) {
		fmt.Print("Yes")
	} else {
		fmt.Print("No")
	}
}
