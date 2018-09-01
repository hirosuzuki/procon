package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scanf("%s\n", &s)
	result := strings.Count(s, "1")
	fmt.Printf("%d\n", result)
}
