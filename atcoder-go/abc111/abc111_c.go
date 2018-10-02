package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

type Pair struct {
	k int
	v int
}

type PairList []Pair

func (a PairList) Len() int {
	return len(a)
}

func (a PairList) Swap(i, j int) {
	a[i], a[j] = a[j], a[i]
}

func (a PairList) Less(i, j int) bool {
	return a[j].v < a[i].v
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func count(vs []int) PairList {
	counter := make(map[int]int)
	for _, v := range vs {
		counter[v]++
	}
	pairs := PairList{Pair{0, 0}}
	for k, v := range counter {
		pairs = append(pairs, Pair{k, v})
	}
	sort.Sort(pairs)
	return pairs
}

func main() {
	n := loadint()

	odd_v := make([]int, n/2)
	even_v := make([]int, n/2)
	for i := 0; i < n/2; i++ {
		odd_v[i] = loadint()
		even_v[i] = loadint()
	}

	odd_counter := count(odd_v)
	even_counter := count(even_v)

	result := n
	if odd_counter[0].k == even_counter[0].k {
		result = n - max(odd_counter[0].v+even_counter[1].v, odd_counter[1].v+even_counter[0].v)
	} else {
		result = n - odd_counter[0].v - even_counter[0].v
	}
	fmt.Println(result)
}
