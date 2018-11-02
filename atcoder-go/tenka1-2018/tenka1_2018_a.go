package main

import (
	"fmt"
)

func stringReverse(s string) string {
	l := len(s)
	cs := make([]rune, l)
	for i, c := range s {
		cs[l-i-1] = c
	}
	return string(cs)
}

func main() {
	var s string
	fmt.Scan(&s)
	if len(s) == 3 {
		s = stringReverse(s)
	}
	fmt.Println(s)
}
