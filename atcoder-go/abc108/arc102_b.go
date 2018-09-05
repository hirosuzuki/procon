package main

import "fmt"

type Edge struct {
	v int
	u int
	n int
}

func main() {
	var l int
	fmt.Scan(&l)
	var m int
	for (l >> uint(m+1)) > 0 {
		m++
	}
	var edges []Edge
	for i := 0; i < m; i++ {
		edges = append(edges, Edge{i + 1, i + 2, 0})
		edges = append(edges, Edge{i + 1, i + 2, 1 << uint(i)})
	}
	b := 1 << uint(m)
	for i := m - 1; i >= 0; i-- {
		d := 1 << uint(i)
		if l-b >= d {
			edges = append(edges, Edge{i + 1, m + 1, b})
			b += d
		}
	}
	fmt.Println(m+1, len(edges))
	for _, e := range edges {
		fmt.Println(e.v, e.u, e.n)
	}
}
