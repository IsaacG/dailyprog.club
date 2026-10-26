"""Tidying a Retrieval Slip

In a records archive, a retrieval slip lists a location as a string of steps, and the clerks tidy each slip before filing it.
Given `path`, a string that starts with '/' and whose steps are separated by one or more '/' characters, return the tidied location.
Blank steps (from doubled or trailing slashes) and steps equal to '.' are skipped.
A step equal to '..' cancels the most recent step still standing, or does nothing if none remain.
Every other step, including ones like '...' or '.hidden', is an ordinary shelf name and is kept exactly as written.
The tidied location starts with '/', joins the remaining names with single '/' characters, and has no trailing '/' unless it is just '/'.

### Constraints

* 1 <= the length of `path` <= 59
"""
import unittest

def tidyLocation(path):
    """Return the canonical form of the path."""
    out = []
    for i in path.split("/"):
        if i == "..":
            if out:
                out.pop()
        elif i != "" and i != ".":
            out.append(i)
    return "/" + "/".join(out)



class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(tidyLocation("/home//foo/./bar/../baz/"), "/home/foo/baz")
        self.assertEqual(tidyLocation("/"), "/")
        self.assertEqual(tidyLocation("/../.."), "/")
        self.assertEqual(tidyLocation("/a/b/"), "/a/b")
        self.assertEqual(tidyLocation("/a/.../b"), "/a/.../b")
        self.assertEqual(tidyLocation("/a/./b/../../c/"), "/c")
        self.assertEqual(tidyLocation("/a/b/../../.."), "/")
        self.assertEqual(tidyLocation("/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z/../../"), "/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x")

if __name__ == "__main__":
    unittest.main()
