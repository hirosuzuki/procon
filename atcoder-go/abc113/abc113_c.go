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

type py struct {
	p    int
	y    int
	rank int
}

func (p py) String() string {
	return fmt.Sprintf("p(%d %d %d)", p.p, p.y, p.rank)
}

type pyList [](*py)

func (p pyList) Len() int {
	return len(p)
}

func (p pyList) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func (p pyList) Less(i, j int) bool {
	return p[i].y < p[j].y
}

func main() {
	loadint()
	m := loadint()
	pys := make([]py, m)
	ps := make(map[int]pyList)
	for i := 0; i < m; i++ {
		p := loadint()
		pys[i].p = p
		pys[i].y = loadint()
		ps[p] = append(ps[p], &pys[i])
	}
	for _, vs := range ps {
		sort.Sort(vs)
		for i, v := range vs {
			(*v).rank = i + 1
		}
	}
	for _, py := range pys {
		fmt.Printf("%06d%06d\n", py.p, py.rank)
	}
}
