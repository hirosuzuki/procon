package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc *bufio.Scanner

func init() {
	sc = bufio.NewScanner(os.Stdin)
	buffsize := 1000000
	buff := make([]byte, buffsize)
	sc.Buffer(buff, buffsize)
	sc.Split(bufio.ScanWords)
}

func loadstr() string {
	sc.Scan()
	return sc.Text()
}

func check(s, t string) bool {
	r := map[byte]byte{}
	for i := 0; i < len(s); i++ {
		c := s[i]
		if v, ok := r[c]; ok {
			if v != t[i] {
				return false
			}
		} else {
			r[c] = t[i]
		}
	}
	return true
}

func main() {
	s := loadstr()
	t := loadstr()
	if check(s, t) && check(t, s) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
