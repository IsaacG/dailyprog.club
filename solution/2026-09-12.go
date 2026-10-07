/*
The Two-Bag Job

Two porters are walking the loot away from a job, one duffel bag each.
They are paid by the piece, so the two bags have to end up holding the same number of pieces: exactly half the pieces each, with every piece going in one bag or the other.
The number of pieces is even.

The array `weights` holds the weights of the pieces, where `weights[i]` is the weight of piece i.
Decide which pieces go in which bag so the two bags weigh as nearly the same as possible, and return the smallest achievable difference between the two total weights.

### Constraints

* The number of pieces is even, at least 2 and at most 32.
* Each piece weighs between 1 and 1000000.
*/
package main

import (
    "fmt"
    "os"
)

func twoBagJob(weights []int) int {
    // return the smallest difference in total weight between two equal-sized loads

    l := len(weights)

    abs := func(a int) int {
        if a > 0 { return a }
        return -a
    }

    var solver func(int, int) int

    solver = func(idx, balance int) int {
        if idx == l {
            return balance
        }
        diff := abs(weights[idx] - weights[idx+1])
        return min(
            solver(idx+2, balance + diff),
            solver(idx+2, abs(balance - diff)),
        )
    }
    return solver(0, 0)
}


func main() {
    testCases := []struct{
        input []int
        want int
    }{
        {[]int{6, 5, 4, 3, 2, 1}, 1},
        {[]int{10, 8, 6, 4}, 0},
        {[]int{9, 2, 2, 2, 2, 2}, 7},
        {[]int{9, 4}, 5},
    }
    for _, tc := range testCases {
        if got := twoBagJob(tc.input); got != tc.want {
            fmt.Println("FAIL", tc.input, got, tc.want)
            os.Exit(1)
        }
    }
    os.Exit(0)
}
