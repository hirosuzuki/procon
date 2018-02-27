package main

import "fmt"

func MakeMatrix(w int, h int) [][]int {
	r := make([][]int, w)
	for x := 0; x < w; x++ {
		r[x] = make([]int, h)
	}
	return r
}

func Solve(N int, K int, X []int, Y []int, C []byte) int {
	K2 := K * 2
	m := MakeMatrix(K*3, K*3)
	for i := 0; i < N; i++ {
		x, y := X[i], Y[i]
		if C[i] == 'W' {
			y += K
		}
		x1, y1 := x%K2, y%K2
		x2, y2 := x1+K, y1+K
		m[x1][y1]++
		m[x2][y2]++
		m[x1][y2]--
		m[x2][y1]--
		x1, y1 = (x+K)%K2, (y+K)%K2
		x2, y2 = x1+K, y1+K
		m[x1][y1]++
		m[x2][y2]++
		m[x1][y2]--
		m[x2][y1]--
	}

	ms := MakeMatrix(K2, K2)
	for y := 0; y < K2; y++ {
		for x := 0; x < K2; x++ {
			c := m[x][y]
			if x > 0 {
				c += ms[x-1][y]
			}
			if y > 0 {
				c += ms[x][y-1]
			}
			if x > 0 && y > 0 {
				c -= ms[x-1][y-1]
			}
			ms[x][y] = c
		}
	}

	rmax := 0
	for y := K; y < K2; y++ {
		for x := K; x < K2; x++ {
			r := ms[x][y]
			if rmax < r {
				rmax = r
			}
			if rmax < N-r {
				rmax = N - r
			}
		}
	}

	return rmax
}

func main() {
	var N int
	var K int
	fmt.Scanf("%d %d\n", &N, &K)
	X := make([]int, N)
	Y := make([]int, N)
	C := make([]byte, N)
	for i := 0; i < N; i++ {
		fmt.Scanf("%d %d %c\n", &X[i], &Y[i], &C[i])
	}
	fmt.Println(Solve(N, K, X, Y, C))
}
