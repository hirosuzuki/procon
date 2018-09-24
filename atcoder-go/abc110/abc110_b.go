package main

import (
	"bufio"
	"fmt"
	"os"
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

func maxints(xs []int) (result int) {
	result = xs[0]
	for _, x := range xs[1:] {
		if result < x {
			result = x
		}
	}
	return
}

func minints(xs []int) (result int) {
	result = xs[0]
	for _, x := range xs[1:] {
		if result > x {
			result = x
		}
	}
	return
}

func main() {
	n := loadint()
	m := loadint()
	x := loadint()
	y := loadint()
	xs := loadints(n)
	ys := loadints(m)
	xs = append(xs, x)
	ys = append(ys, y)
	if maxints(xs) >= minints(ys) {
		fmt.Print("War")
	} else {
		fmt.Print("No War")
	}
}
