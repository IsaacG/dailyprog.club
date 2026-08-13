/*
The Fourth-Floor Corridor

The fourth floor has one corridor, and it is exactly one trolley wide.

At five o'clock the post room lets every mail trolley go at once.
The trolleys stand in a line running from the west end of the corridor to the east end, and `trolleys[i]` is the i-th of them: the number is positive if that trolley was pushed east and negative if it was pushed west, and its size is how many sacks of mail the trolley carries.
Every trolley rolls at the same pace, so two trolleys pushed the same way never meet.

When a trolley rolling east comes up against a trolley rolling west, the corridor is too narrow for both to pass:

* If one of them carries more sacks than the other, that one has right of way.
The lighter trolley's sacks are tipped onto it, so from then on it carries both loads, and the emptied trolley is wheeled into a side room.
* If the two carry the same number of sacks, neither yields.
Both are wheeled into side rooms, and their mail is sent down to the sorting desk.

A trolley that has taken on extra sacks keeps rolling the way it was already going, heavier than it was, and may come up against another trolley further along.

Return the load of every trolley still rolling once no two of them can meet again, listed from the west end to the east end, using the same sign convention.

Constraints:

* `0 <= n <= 200`, where `n` is the number of trolleys
* each entry of `trolleys` is between -1000 and 1000, and is never 0
*/
package main

import (
	"fmt"
	"os"
	"slices"
)

// Return the load of each trolley still rolling, west to east.
func settleCorridor(trolleys []int) []int {
	res := []int{}
	for _, next := range trolleys {
		for len(res) > 0 && res[len(res)-1] > 0 && next < 1 {
			prior := res[len(res)-1]
			res = res[:len(res)-1]
			if prior == -next {
				next = 0
			} else {
				new := prior - next
				if -next > prior {
					new *= -1
				}
				next = new
			}
		}
		if next != 0 {
			res = append(res, next)
		}
	}
	return res
}

func main() {
    testCases := []struct{input, want []int}{
        {[]int{5, -2, 3},     []int{7, 3}},
        {[]int{-4, 2, -6, 1}, []int{-4, -8, 1}},
        {[]int{6, -6, 2},     []int{2}},
        {[]int{5, 2, -3},     []int{}},
    }
    for _, tc := range testCases {
        got := settleCorridor(tc.input)
		fmt.Println(tc, got)
		if !slices.Equal(got, tc.want) {
            println("FAIL", tc.input, got, tc.want)
            os.Exit(1)
        } else {
			println("PASS")
		}
    }
    os.Exit(0)
}
