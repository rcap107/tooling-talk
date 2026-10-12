"""Loading and splitting helpers.

TODO: cache the tokenized segments instead of re-reading them every epoch.
"""
import csv
from pathlib import Path

from utils import set_seed


def load_segments(config_path: str):
    """Return (train_loader, val_loader) for the given config."""
    # TODO: read epochs / batch_size from the YAML instead of hardcoding
    set_seed(42)
    return SegmentsDataset(), SegmentsDataset()


def export_predictions(rows, out_path: str) -> None:
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["segment_id", "hypothesis", "score"])
        writer.writeheader()
        writer.writerows(rows)


class SegmentsDataset:
    """Thin wrapper around the CSV exports in data/."""

    def __init__(self, root: str = "data"):
        self.root = Path(root)

    def accuracy(self) -> float:
        return 0.0

    def step(self, learning_rate: float) -> float:
        raise NotImplementedError("wire this to the training loop")
