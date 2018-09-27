package main

import (
	"bufio"
	"fmt"
	"math"
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
	xs := make([]int, n)
	ys := make([]int, n)
	for i := 0; i < n; i++ {
		xs[i] = loadint()
		ys[i] = loadint()
	}
	dmax := (xs[0]-xs[1])*(xs[0]-xs[1]) + (ys[0]-ys[1])*(ys[0]-ys[1])
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			d := (xs[i]-xs[j])*(xs[i]-xs[j]) + (ys[i]-ys[j])*(ys[i]-ys[j])
			if d > dmax {
				dmax = d
			}
		}
	}
	result := math.Sqrt(float64(dmax))
	fmt.Println(result)
}
