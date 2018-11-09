package main

import (
	"fmt"
)

func main() {
	var x, y int
	fmt.Scan(&x, &y)
	result := x + y/2
	fmt.Println(result)
}
