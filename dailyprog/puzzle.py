#!/usr/bin/env python3
"""Helper to access https://beta.dailyprog.club/ puzzles."""

import argparse
import copy
import datetime
import importlib
import json
import os
import pathlib
import re
import subprocess
import sys
import uuid

from lxml import etree, html
import markdownify
import more_itertools
import requests

import sign


class Puzzle:
    """Puzzle presents an interface to interact with the dailyprog.club puzzle."""

    def __init__(self, language: str, date: datetime.date | None = None, cache_dir: pathlib.Path | None = None) -> None:
        """Initialize the puzzle.

        date: the puzzle to load. If set to None, use today.
        cache_dir: override where HTML files should be cached.
        """
        today = datetime.datetime.now(tz=datetime.UTC).date()
        if date is None:
            date = today
        if date > today:
            raise ValueError(f"Cannot read the future, {date=}")
        self.date = date
        self.date_str = self.date.strftime("%Y-%m-%d")
        self.url = f"https://beta.dailyprog.club/en/puzzle/{self.date_str}"
        self.language = language

        cache_dir_options = [
            (os.getenv("XDG_CACHE_HOME", "/"), "dailyprog.club"),
            (os.environ["HOME"], ".cache"),
            (os.getcwd(), "cache"),
        ]
        if cache_dir is None:
            for root, name in cache_dir_options:
                i = pathlib.Path(root) / name
                if i.exists():
                    cache_dir = i
                    break

        self.cache_dir = cache_dir
        self._load()

    def _html(self) -> str:
        """Return the puzzle as HTML, using caching if specified."""
        if self.cache_dir and self.cache_dir.exists():
            cache_file = (self.cache_dir / self.date_str).with_suffix(".html")
            if cache_file.exists():
                return cache_file.read_text()

        resp = requests.get(self.url)
        resp.raise_for_status()

        if self.cache_dir and self.cache_dir.exists():
            cache_file = (self.cache_dir / self.date_str).with_suffix(".html")
            cache_file.write_text(resp.text)

        return resp.text

    def _load(self) -> None:
        """Load the puzzle data."""
        root = etree.HTML(self._html())
        self.tests = list(more_itertools.chunked(root.xpath("//figure/pre/code/text()"), 2))
        self.title = root.xpath('//h1[@id="puzzle-title"]/text()')[0]
        self.description = root.xpath("//div/div/div/section")[0]

        i = next(
            i
            for i in root.xpath("//html/body/script/text()")
            if "starterCode" in i
        )
        i = json.loads(i[i.index("(") + 1:-1])[1]
        i = json.loads(i[i.index(":") + 1:])[-1]["children"][2][3]
        for key in ["id", "number", "difficulty", "title", "functionName", "starterCode", "visibleTests", "timeLimitMs"]:
            setattr(self, key, i[key])

    def solution_dir(self) -> str:
        """Return the path containing the solutions."""
        return pathlib.Path(__file__).resolve().parent.parent / "solution"

    def solution_module(self) -> module:
        """Return the solution module."""
        if str(self.solution_dir()) not in sys.path:
            sys.path.append(str(self.solution_dir()))
        return importlib.import_module(self.date_str)

    def solution_file(self) -> pathlib.Path:
        """Return the solution file."""
        suffix = {"python": ".py", "go": ".go"}[self.language]
        return (self.solution_dir() / self.date_str).with_suffix(suffix)

    def write_solution_stub(self) -> None:
        """Populate the solution file with the starter code."""
        {"python": self.write_solution_stub_python, "go": self.write_solution_stub_go}[self.language]()

    def write_solution_stub_go(self) -> None:
        file = self.solution_file()
        if file.exists():
            return

        out = []
        desc = self.markdown().splitlines()
        out.append('/*')
        out.append(desc[0])
        out.extend(desc[2:])
        out.append('*/')
        out.append("package main")
        out.append("")
        out.append('import "os"')
        out.append("")
        out.append(self.starterCode["go"])
        out.append("")
        out.append("func main() {")
        out.append("    testCases := []struct{input, want string}{")
        for a, b in self.tests:
            out.append(f"        {{{a}, {b}}},")
        out.append("    }")
        out.append("    for _, tc := range testCases {")
        out.append(f"        if got := {self.functionName()}(tc.input); got != tc.want {{")
        out.append('            println("FAIL", tc.input, got, tc.want)')
        out.append("            os.Exit(1)")
        out.append("        }")
        out.append("    }")
        out.append('    os.Exit(0)')
        out.append("}")
        file.write_text("\n".join(out).strip() + "\n")

    def write_solution_stub_python(self) -> None:
        file = self.solution_file()
        if file.exists():
            return

        out = []
        desc = self.markdown().splitlines()
        out.append('"""' + desc[0])
        out.extend(desc[2:])
        out.append('"""')
        out.append("import unittest")
        out.append("")
        out.append(self.starterCode[self.language])
        out.append("")
        out.append("class TestSolution(unittest.TestCase):")
        out.append("    def test_data(self):")
        for a, b in self.tests:
            out.append(f"        self.assertEqual({a}, {b})")
        out.append("")
        out.append('if __name__ == "__main__":')
        out.append("    unittest.main()")

        file.write_text("\n".join(out).strip() + "\n")

    def solution_code(self) -> str:
        """Return the solution code."""
        return self.solution_file().read_text()

    def markdown(self) -> str:
        """Return the puzzle description as markdown."""
        clean_html = html.tostring(self.description, encoding="utf-8").decode("utf-8")
        lines = markdownify.markdownify(clean_html).splitlines()
        if lines[0].endswith("till reset"):
            lines.pop(0)
        while not lines[0]:
            lines.pop(0)
        if lines[0] == f"#{self.number}":
            lines.pop(0)
        while not lines[0]:
            lines.pop(0)
        out = "\n".join(lines)
        out = re.sub(r"\. ([A-Z])", (lambda m: ".\n" + m.group(1)), out)
        return out

    def test(self) -> bool:
        """Run the visible tests, returning if the solution passes and a report."""
        cmd = {
            "python": ["python", self.solution_file()],
            "go": ["go", "run", self.solution_file()],
        }[self.language]
        p = subprocess.run(cmd)
        return p.returncode == 0

    def submit(self):
        """Submit the solution. WIP."""
        signature = sign.sign_submission(self.id, self.solution_code())
        data = {
            "id": self.id,
            "code": self.solution_code(),
            "language": self.language,
            "submission": signature,
            "attemptNo": 1,
        }
        headers = {
            "referer": f"https://beta.dailyprog.club/en/puzzle/{self.date_str}",
            "origin": "https://beta.dailyprog.club",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
        }

        resp = requests.post("https://beta.dailyprog.club/api/verify", json=data, headers=headers)
        resp.raise_for_status()
        return resp.json()


def main() -> None:
    # Parse args.
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", "-d")
    parser.add_argument("--show", "-s", action="store_true")
    parser.add_argument("--verify", "-v", action="store_true")
    parser.add_argument("--language", "-l", default="python")
    args = parser.parse_args()

    # Puzzle date. Default to None/today.
    date = None
    if args.date:
        date = datetime.date.strptime(args.date, "%Y-%m-%d")

    p = Puzzle(language=args.language, date=date)
    p.write_solution_stub()

    # Print the puzzle description.
    if args.show:
        print(p.markdown())
        print("\n----\n")

    print("Testing...")
    if not p.test():
        return

    # Submit the solution to run the hidden tests.
    if args.verify:
        print("Verifying...")
        result = p.submit()
        print("PASSED" if result["passed"] else "FAILED")
        if not result["passed"]:
            print(result)


if __name__ == "__main__":
    main()
