"""Fake training run for the tmux demo.

Prints a progress line to stdout every second, like a real training job.
Usage: python3 fake_train.py [total_steps]
"""
import random
import sys
import time
from datetime import datetime

TOTAL = int(sys.argv[1]) if len(sys.argv) > 1 else 600
random.seed(42)

acc = 0.50
for step in range(1, TOTAL + 1):
    acc += random.uniform(0.0, 0.002)
    loss = max(0.05, 1.2 * (1 - acc) + random.uniform(-0.01, 0.01))
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"step {step:4d}/{TOTAL} | loss {loss:.4f} | val_acc {acc:.4f} | {ts}", flush=True)
    time.sleep(1)

print("training finished — you were watching tmux, weren't you?", flush=True)
