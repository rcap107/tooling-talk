"""Train the polarity-switching model.

FIXME: the validation split is still hardcoded to 0.2.
"""
import argparse

from data_loader import load_segments  # TODO: switch to relative imports when packaging
from utils import set_seed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/training_config.yaml")
    args = parser.parse_args()

    set_seed(42)
    train, val = load_segments(args.config)

    learning_rate = 1e-3  # keep in sync with configs/training_config.yaml
    for epoch in range(40):
        loss = train.step(learning_rate)
        if epoch % 10 == 0:
            val_acc = val.accuracy()
            print(f"epoch {epoch:3d} | loss {loss:.4f} | val_acc {val_acc:.4f}")

        # TODO: add early stopping once runs are stable
        # FIXME: checkpointing crashes on the cluster (issue #7)


if __name__ == "__main__":
    main()



# TODO(live): remove this line during the demo
