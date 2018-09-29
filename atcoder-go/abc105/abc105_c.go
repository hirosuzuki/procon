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

func calc(n int) string {
	if n == 0 {
		return "0"
	}

	r := ""
	k := 1
	for n != 0 {
		if (n & 1) == 1 {
			n -= k
			r = "1" + r
		} else {
			r = "0" + r
		}
		n >>= 1
		k = -k
	}

	return r
}

func main() {
	n := loadint()
	fmt.Println(calc(n))
}
