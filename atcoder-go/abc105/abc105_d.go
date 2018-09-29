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
	buffsize := 1000000
	buff := make([]byte, buffsize)
	sc.Buffer(buff, buffsize)
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
	m := loadint()
	as := loadints(n)
	ms := make(map[int]int)
	t := 0
	ms[t]++
	for _, a := range as {
		t = (t + a) % m
		ms[t]++
	}
	result := 0
	for _, r := range ms {
		result += r * (r - 1) / 2
	}
	fmt.Println(result)
}
