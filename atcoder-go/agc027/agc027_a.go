package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc *bufio.Scanner

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
}

func loadint() (result int) {
	sc.Scan()
	result, _ = strconv.Atoi(sc.Text())
	return
}

func loadints(n int) []int {
	xs := make([]int, n)
	for i := 0; i < n; i++ {
		xs[i] = loadint()
	}
	return xs
}

func main() {
	n := loadint()
	x := loadint()
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
