package main

import (
	"fmt"
)

func main() {
	var h, w, k int
	fmt.Scan(&h, &w, &k)

	var patterns = [][]int{{0}}
	for i := 1; i < w; i++ {
		var patternsNext = [][]int{}
		for _, pattern := range patterns {
			patternN := make([]int, i+1)
			copy(patternN, pattern)
			patternN[i] = i
			patternsNext = append(patternsNext, patternN)
			if pattern[i-1] == i-1 {
				patternR := make([]int, i+1)
				copy(patternR, pattern)
				patternR[i-1] = i
				patternR[i] = i - 1
				patternsNext = append(patternsNext, patternR)
			}
		}
		patterns = patternsNext
	}

	nums := make([]int, w)
	nums[0] = 1
	for i := 0; i < h; i++ {
		numsNext := make([]int, w)
		for _, pattern := range patterns {
			for i, n := range pattern {
				numsNext[i] = (numsNext[i] + nums[n]) % 1000000007
			}
		}
		nums = numsNext
	}
	fmt.Println(nums[k-1])

}
