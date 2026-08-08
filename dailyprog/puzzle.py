#!/usr/bin/env python3
"""Helper to access https://beta.dailyprog.club/ puzzles."""

import argparse
import datetime
import importlib
import json
import os
import pathlib
import requests
import sys
import uuid

from lxml import etree, html
import markdownify
import more_itertools

import sign


class Puzzle:
    """Puzzle presents an interface to interact with the dailyprog.club puzzle."""

    def __init__(self, date: datetime.date | None = None, cache_dir: pathlib.Path | None = None) -> None:
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
        return (self.solution_dir() / self.date_str).with_suffix(".py")

    def write_solution_stub(self) -> None:
        """Populate the solution file with the starter code."""
        file = self.solution_file()
        if file.exists():
            return
        file.write_text(self.starterCode["python"])

    def solution_code(self) -> str:
        """Return the solution code."""
        return self.solution_file().read_text()

    def markdown(self) -> str:
        """Return the puzzle description as markdown."""
        clean_html = html.tostring(self.description, encoding="utf-8").decode("utf-8")
        lines = markdownify.markdownify(clean_html).splitlines()
        if lines[0].endswith("till reset"):
            lines = lines[2:]
        return "\n".join(lines)

    def test(self) -> tuple[bool, list[str]]:
        """Run the visible tests, returning if the solution passes and a report."""
        passes = True
        report = []
        func = getattr(self.solution_module(), self.functionName)
        for i, test in enumerate(self.visibleTests):
            got = func(*test["args"])
            want = test["expected"]
            result = "PASS" if got == want else "FAIL"
            report.append(f"{i} {result} - {test["name"]}")
            report.append(f"  Want {self.functionName}({", ".join(str(i) for i in test["args"])}) == {test["expected"]}")
            if got != want:
                report.append(f"  Got  {got}")
                passes = False
        return passes, report

    def submit(self):
        """Submit the solution. WIP."""
        signature = sign.sign_submission(self.id, self.solution_code())
        data = {
            "id": self.id,
            "code": self.solution_code(),
            "language": "python",
            "submission": signature,
        }
        headers = {
            "referer": "https://beta.dailyprog.club/en/puzzle/2026-08-05",
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
    parser.add_argument("--verify", "-v", action="store_true")
    args = parser.parse_args()

    # Puzzle date. Default to None/today.
    date = None
    if args.date:
        date = datetime.date.strptime(args.date, "%Y-%m-%d")

    p = Puzzle(date)
    p.write_solution_stub()

    # Print the puzzle description.
    print(p.markdown())
    print("\n----\n")

    print("Testing...")
    passes, report = p.test()
    print("\n".join(report))

    if not passes:
        return

    # Submit the solution to run the hidden tests.
    if args.verify:
        result = p.submit()
        if not result["passed"]:
            return

    # Update the code file to include the puzzle prose and tests.
    if p.solution_code().startswith('"""'):
        return
    desc = p.markdown().splitlines()
    out = []
    out.append('"""' + desc[0])
    out.extend(desc[2:])
    out.append('"""')
    out.append(p.solution_code())
    for a, b in p.tests:
        out.append(f"assert {a} == {b}")
    p.solution_file().write_text("\n".join(out).strip() + "\n")


if __name__ == "__main__":
    main()
