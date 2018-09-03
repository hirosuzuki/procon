package main

import (
	"fmt"
	_ "strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	var words = []string{"dream", "dreamer", "erase", "eraser"}
	i := len(s)
	var result bool
	for i > 0 {
		result = false
		for _, w := range words {
			l := len(w)
			j := i - l
			if j >= 0 && s[j:i] == w {
				result = true
				i = j
				break
			}
		}
		if !result {
			break
		}
	}
	if result {
		fmt.Print("YES")
	} else {
		fmt.Print("NO")
	}
}
