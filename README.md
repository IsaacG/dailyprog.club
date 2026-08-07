# dailyprog.club

Framework and solutions for dailyprob.club puzzles

```bash
» ./dailyprog/puzzle.py -d 2026-08-03
#46

Festival Banners
================

At a harvest festival, each stall keeps its apple count in the array `baskets`. To help visitors compare, every stall hangs a banner showing the product of the apple counts of every *other* stall.

Return an array where `result[i]` is the number shown on stall `i`'s banner.

Constraints:

* `1 <= n <= 10`, where `n` is the length of `baskets`
* Each count is an integer from `0` to `9`
* The product of an empty set of counts is `1`

----

Testing...
PASS  otherProducts([2, 3, 4]) -> [12, 8, 6]
PASS  otherProducts([1, 5]) -> [5, 1]
```

## Key Pair Generation

An ED25519 keypair is used to sign submissions to the site's REST API.
The site writes the private key to the browser's storage in a non-exportable manner.
So get the key, we need to regenerate it from the passphrase.

Use the Claude generated `getKeypair.mjs` code to generate your ED25519 key from your twenty four word passphrase.
Write the result to `XDG_DATA_HOME`.

```bash
# Check out the dailyprog code.
git clone https://codeberg.org/dailyprog/dailyprog.club.git site
# Copy the getKeypair.mjs into that workspace.
cp getKeypair.mjs site/workspaces/app/scripts/getKeypair.mjs
# Set up directories.
cd site/workspaces/app
mkdir "${XDG_DATA_HOME}/dailyprog.club"
# Generate the ED25519 keys.
corepack pnpm exec tsx scripts/getKeypair.mjs 'your twenty four word passphase' "${XDG_DATA_HOME}/dailyprog.club/keys.json"
```
