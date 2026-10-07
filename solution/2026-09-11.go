/*
Balancing the Spin Ring

The ring station keeps its footing by spinning, and the rim is lined with cradles.
Every cradle takes exactly two ballast canisters, and a cradle only holds the spin steady when the two canisters clamped into it add up to at least `limit` kilograms.
A cradle lighter than that lets the ring wobble.

The array `weights` holds the mass of each canister in kilograms, where `weights[i]` is the mass of canister i.
Every canister must be clamped into exactly one cradle, two canisters to a cradle, and a canister is never split or left out.

Return `true` if the canisters can be seated so that every cradle's combined mass is at least `limit`, and `false` otherwise.
Because a cradle takes exactly two canisters, an odd number of canisters can never be seated.

### Constraints

* `1 <= n <= 24`, where `n` is the number of canisters in `weights`
* each mass is an integer in `[1, 10^9]`
* `1 <= limit <= 10^9`
*/
package main

import (
	"fmt"
	"os"
)

func canBalanceRing(weights []int, limit int) bool {
	// return true if every canister can be seated two per cradle, each cradle at least limit.
	l := len(weights)
	for i := range l / 2 {
		if weights[i] + weights[l - 1 - i] < limit {
			return false
		}
	}
	return true
}


func main() {
    testCases := []struct{
	    weights []int
	    limit int
	    want bool
    }{
        {[]int{}, 90, true},
        {[]int{40,50,50,60,60,70}, 90, true},
        {[]int{10,20,30,40}, 60, false},
        {[]int{40,50,50,50,50,60,60,60}, 90, true},
        {[]int{100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100}, 150, true},
    }
    for _, tc := range testCases {
        if got := canBalanceRing(tc.weights, tc.limit); got != tc.want {
            fmt.Println("FAIL", tc.weights, tc.limit, got, tc.want)
            os.Exit(1)
        }
    }
    os.Exit(0)
}
