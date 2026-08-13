package main

import "strings"

// Return the sheet Hesper's press would produce
func setType(manuscript string) string {
	var sb strings.Builder
	shifts := make(map[rune]int)
	for _, c := range manuscript {
		sb.WriteRune('a' + rune((int(c - 'a') + shifts[c]) % 26))
		shifts[c]++
	}
	return sb.String()
}

func main() {
	testCases := []struct{input, want string}{
		{"abc", "abc"},
		{"aaa", "abc"},
		{"aab", "abb"},
		{"banana", "banboc"},
		{"zz", "za"},
	}
	for _, tc := range testCases {
		if got := setType(tc.input); got != tc.want {
			println("FAIL", tc.input, got, tc.want)
			break
		}
	}
	println("PASS")
}
