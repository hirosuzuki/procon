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

func abs(x int) int {
	if x > 0 {
		return x
	}
	return -x
}

func solve(n int, xs, ys []int) {
	maxd := 0
	evendCount := 0
	for i := 0; i < n; i++ {
		d := abs(xs[i]) + abs(ys[i])
		if d > maxd {
			maxd = d
		}
		if d%2 == 0 {
			evendCount++
		}
	}

	if evendCount != 0 && evendCount != n {
		fmt.Println(-1)
		return
	}

	var l int
	for l = 0; (1 << uint(l)) <= maxd; l++ {
	}

	var armlen []int

	if evendCount > 0 {
		armlen = append(armlen, 1)
	}
	for i := 0; i < l; i++ {
		armlen = append(armlen, 1<<uint(l-i-1))
	}

	fmt.Println(len(armlen))

	for i := 0; i < len(armlen); i++ {
		fmt.Print(armlen[i], " ")
	}
	fmt.Println()

	for i := 0; i < n; i++ {
		x := 0
		y := 0
		for j := 0; j < len(armlen); j++ {
			cmd := "R"
			if j == 0 && evendCount > 0 {
				cmd = "R"
				x++
			} else {
				dx := xs[i] - x
				dy := ys[i] - y
				if dx > dy {
					if dx > -dy {
						cmd = "R"
						x += armlen[j]
					} else {
						cmd = "D"
						y -= armlen[j]
					}
				} else {
					if dx > -dy {
						cmd = "U"
						y += armlen[j]
					} else {
						cmd = "L"
						x -= armlen[j]
					}
				}
			}
			fmt.Print(cmd)
		}
		fmt.Println()
	}

}

func main() {
	n := loadint()

	x := make([]int, n)
	y := make([]int, n)

	for i := 0; i < n; i++ {
		x[i] = loadint()
		y[i] = loadint()
	}

	solve(n, x, y)
}
