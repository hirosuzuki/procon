package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

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
	var n, x int
	fmt.Scan(&n, &x)
	a := loadints(n)
	sort.Ints(a)
	result := 0
	for i := 0; i < n; i++ {
		if (x >= a[i] && i < n-1) || (x == a[i]) {
			x -= a[i]
			result++
		}
	}
	fmt.Println(result)
}
