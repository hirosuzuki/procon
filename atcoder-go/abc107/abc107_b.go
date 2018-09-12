package main

import (
	"fmt"
)

func main() {
	var h, w int
	fmt.Scan(&h, &w)
	a := make([][]byte, h)
	ys := make([]bool, h)
	xs := make([]bool, w)
	for i := 0; i < h; i++ {
		var s string
		fmt.Scan(&s)
		a[i] = make([]byte, w)
		for j := 0; j < w; j++ {
			a[i][j] = s[j]
			if s[j] == '#' {
				ys[i] = true
				xs[j] = true
			}
		}
	}
	for i := 0; i < h; i++ {
		if ys[i] {
			for j := 0; j < w; j++ {
				if xs[j] {
					fmt.Printf("%c", a[i][j])
				}
			}
			fmt.Println()
		}
	}
}
