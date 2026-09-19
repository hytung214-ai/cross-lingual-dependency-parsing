#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPARISON = ROOT / "results" / "root_compare.tsv"


def main() -> None:
    totals = {"en-zh": 0, "ja-zh": 0}
    correct = {"en-zh": 0, "ja-zh": 0}

    with COMPARISON.open(encoding="utf-8") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            values = dict(field.split("=", 1) for field in fields[1:])
            gold = values["gold"]
            for system in totals:
                totals[system] += 1
                correct[system] += values[system] == gold

    for system in totals:
        accuracy = correct[system] / totals[system]
        print(
            f"{system}: {correct[system]}/{totals[system]} "
            f"correct roots ({accuracy:.2%})"
        )


if __name__ == "__main__":
    main()

