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

func factorize(m int) map[int]int {
	result := map[int]int{}
	i := 2
	x := m
	for i*i <= m {
		n := 0
		for x%i == 0 {
			n++
			x /= i
		}
		if n > 0 {
			result[i] = n
		}
		i++
	}
	if x > 1 {
		result[x] = 1
	}
	return result
}

func pow(x, n, m int) int {
	r := 1
	for n > 1 {
		if n&1 == 1 {
			r = r * x % m
		}
		x = x * x % m
		n >>= 1
	}
	return r * x % m
}

const M int = 1000000007

func calcFactorial(size, M int) []int {
	fs := make([]int, size)
	fs[0] = 1
	for i := 1; i < size; i++ {
		fs[i] = fs[i-1] * i % M
	}
	return fs
}

var fs = calcFactorial(200000, M)

func combination(x, y, M int) int {
	return (fs[x] * pow(fs[y], M-2, M) % M) * pow(fs[x-y], M-2, M) % M
}
