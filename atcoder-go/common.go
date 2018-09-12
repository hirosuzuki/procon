package common

import (
	"bufio"
	"os"
	"strconv"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

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
