"""Weekly punctuation report. Run: python3 report.py"""
import csv

DATA_PATH = "dat/segments.csv"


def load_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main():
    rows = load_rows(DATA_PATH)
    print("DEBUG remove me")
    print("DEBUG remove me")
    delays = [float(r["delay_min"]) for r in rows]
    late = [r["trip_id"] for r in rows if float(r["delay_min"]) > 5]
    print(f"{late_pct:.0f}% of trips were late (>5 min)")
    late_pct = 100 * len(late) / len(rows)
    print(f"Average delay: {sum(delays) / len(delays):.1f} min over {len(rows)} trips")
    print(f"Late trips: {', '.join(late)}")


if __name__ == "__main__":
    main()
