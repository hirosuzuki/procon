package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	result := strings.Count(s, "1")
	fmt.Print(result)
}
