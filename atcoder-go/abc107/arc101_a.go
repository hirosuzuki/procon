package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func loadints(n int) []int {
	xs := make([]int, n)
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	for i := 0; i < n; i++ {
		sc.Scan()
		xs[i], _ = strconv.Atoi(sc.Text())
	}
	return xs
}

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	x := loadints(n)
	result := 100000000000
	for i := 0; i < n-k+1; i++ {
		d := x[i+k-1] - x[i]
		m := min(abs(x[i+k-1]), abs(x[i]))
		r := d + m
		result = min(r, result)
	}
	fmt.Println(result)
}
