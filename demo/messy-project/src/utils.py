"""Small shared helpers.

XXX: this module is becoming a dumping ground, split it before the paper.
"""
import random


def set_seed(seed: int) -> None:
    random.seed(seed)


def maybe_debug(x):
    # XXX: left over from debugging, do not ship
    if x is None:
        return []
    return x
