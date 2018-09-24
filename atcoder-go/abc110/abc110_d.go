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

func main() {
	n := loadint()
	m := loadint()
	fs := factorize(m)
	result := 1
	for _, y := range fs {
		result = result * combination(n+y-1, y, M) % M
	}
	fmt.Println(result)
}
