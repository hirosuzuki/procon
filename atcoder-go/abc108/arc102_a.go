package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	var result int
	if k%2 == 1 {
		i := n / k
		result = i * i * i
	} else {
		i := n / k
		j := (n + k/2) / k
		result = i*i*i + j*j*j
	}
	fmt.Println(result)
}
