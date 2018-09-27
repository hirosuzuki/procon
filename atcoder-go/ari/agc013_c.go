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

func main() {
	n := loadint()
	l := loadint()
	t := loadint()
	xs := make([]int, n)
	ws := make([]int, n)
	for i := 0; i < n; i++ {
		xs[i] = loadint()
		ws[i] = loadint()
	}
	rs := make([]int, n)
	for i := 0; i < n; i++ {
		r := xs[i]
		if ws[i] == 1 {
			r += t
		} else {
			r -= t
		}
		r %= l
		rs[i] = r
	}
	for i := 0; i < n; i++ {
		fmt.Println(rs[i])
	}
}
