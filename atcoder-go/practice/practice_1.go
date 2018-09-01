package main

import (
	"fmt"
)

func main() {
	var a, b, c int64
	var s string
	fmt.Scanf("%d\n", &a)
	fmt.Scanf("%d %d\n", &b, &c)
	fmt.Scanf("%s", &s)
	fmt.Printf("%d %s\n", a+b+c, s)
}
