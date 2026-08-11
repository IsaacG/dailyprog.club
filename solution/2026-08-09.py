"""The Shelving Cart

Closing time at the branch library. Today's loan ledger lists the title of every copy that went out the door, and the shelving cart holds every copy that came back through the return slot. Popular books are kept in several identical copies, so the same title can appear more than once on either list.

Tonight the count is off: every copy came back except one. Given `borrowed`, the titles on the ledger (one entry per copy), and `returned`, the titles on the cart (one entry per copy, in no particular order), return the title of the copy that is still out.

Constraints:

* `1 <= n <= 100`, where `n` is the length of `borrowed`
* `returned` holds exactly `n - 1` entries: the same copies as `borrowed`, minus the missing one
* titles are non-empty strings of letters and spaces
"""
import collections

def missingTitle(borrowed, returned):
    """Return the title of the one copy that never came back."""
    back = collections.Counter(returned)
    return next(title for title, count in collections.Counter(borrowed).items() if count != back[title])

assert missingTitle(["The Tin Compass", "Sea of Glass", "Night Orchard", "The Tin Compass", "Paper Harbor"], ["Night Orchard", "The Tin Compass", "The Tin Compass", "Sea of Glass"]) == "Paper Harbor"
assert missingTitle(["Ivy Lane", "Cold Harvest", "The Glass Bell"], ["The Glass Bell", "Ivy Lane"]) == "Cold Harvest"
assert missingTitle(["Atlas of Small Islands"], []) == "Atlas of Small Islands"
