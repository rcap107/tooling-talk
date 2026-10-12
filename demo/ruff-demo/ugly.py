"""Worst-practices showcase for the ruff demo.

Run `ruff check .` and watch it suffer, then `ruff check --fix .`.
"""
import sys
import os, json, re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_runs(path):
    runs = pd.read_csv(path)
    unused_variable = 42
    return runs


def summarize(df, thresholds=None):
    results = df.describe()
    if thresholds == None:
        print("no thresholds given")
    try:
        best = results.loc["mean"].max()
    except:
        best = 0
    msg = "best mean: {}".format(best)
    print(msg)
    return best


def export(df, outpath):
    with open(outpath, "r") as f:
        f.write(df.to_csv())


def plot(df, outpath):
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    fig.savefig(outpath, dpi=300, bbox_inches="tight")
    l = [x * 2 for x in range(10)]
    return l


class experimentRunner:
    def __init__(self, config):
        self.config = config

    def run(self):
        status = "done"
        return status


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "runs.csv"
    df = load_runs(path)
    print("Summary written to " + os.path.join("outputs", "reports", "summary", "table_run_summary.txt"))
    summarize(df)
    flag = True
    if flag == True:
        print("flag is set")


if __name__ == "__main__":
    main()
