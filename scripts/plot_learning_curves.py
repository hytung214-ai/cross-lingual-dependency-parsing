#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
SCORES = ROOT / "results" / "scores.csv"
FIGURES = ROOT / "figures"


def main() -> None:
    by_system = defaultdict(list)
    with SCORES.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            by_system[row["system"]].append(
                {
                    "epoch": int(row["epoch"]),
                    "UAS": float(row["UAS"]),
                    "LAS": float(row["LAS"]),
                }
            )

    FIGURES.mkdir(exist_ok=True)
    for metric in ("LAS", "UAS"):
        plt.figure()
        for system, rows in sorted(by_system.items()):
            rows.sort(key=lambda item: item["epoch"])
            plt.plot(
                [item["epoch"] for item in rows],
                [item[metric] for item in rows],
                label=system,
            )
        plt.xlabel("Epoch")
        plt.ylabel(metric)
        plt.legend()
        plt.tight_layout()
        output = FIGURES / f"learning_curve_{metric.lower()}.png"
        plt.savefig(output, dpi=200)
        plt.close()
        print(f"Wrote {output}")


if __name__ == "__main__":
    main()

