package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	ws := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&ws[i])
	}
	result := true
	for i := 1; i < n; i++ {
		if ws[i][0] != ws[i-1][len(ws[i-1])-1] {
			result = false
		}
		for j := 0; j < i; j++ {
			if ws[i] == ws[j] {
				result = false
			}
		}
		if result == false {
			break
		}
	}
	if result {
		fmt.Print("Yes")
	} else {
		fmt.Print("No")
	}
}
