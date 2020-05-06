package main

import "fmt"

func main() {
	var x int
	fmt.Scan(&x)
	m := 120
	ns := make([]int, m)
	n5s := make(map[int]int)
	for i := 0; i < m; i++ {
		n := i * i * i * i * i
		ns[i] = n
		n5s[n] = i
	}

	result1 := 0
	result2 := 0

	for i := range ns {
		b := ns[i]
		if a, ok := n5s[b+x]; ok {
			result1, result2 = a, i
			break
		}
		if a, ok := n5s[x-b]; ok {
			result1, result2 = i, -a
			break
		}
	}

	fmt.Println(result1, result2)

}
