"""Intercoder reliability helpers for curator scoring."""

from __future__ import annotations

from collections import Counter
from typing import Iterable, Sequence


def agreement_within_one(a: Sequence[float], b: Sequence[float]) -> float:
    if not a:
        return 1.0
    if len(a) != len(b):
        raise ValueError("Score vectors must be the same length")
    hits = sum(1 for left, right in zip(a, b) if abs(left - right) <= 1.0)
    return hits / len(a)


def percent_within_one_point(
    scorer_a: dict[str, float],
    scorer_b: dict[str, float],
) -> float:
    """Return the share of matching fields whose scores differ by <= 1 point."""

    shared = sorted(set(scorer_a) & set(scorer_b))
    if not shared:
        return 0.0
    hits = sum(1 for key in shared if abs(float(scorer_a[key]) - float(scorer_b[key])) <= 1.0)
    return hits / len(shared)


def cohens_kappa(labels_a: Sequence[str | bool | int], labels_b: Sequence[str | bool | int]) -> float:
    """Cohen's kappa for two equal-length categorical label sequences."""
    if len(labels_a) != len(labels_b):
        raise ValueError("Label vectors must be the same length")
    n = len(labels_a)
    if n == 0:
        return 1.0

    a = [str(x) for x in labels_a]
    b = [str(x) for x in labels_b]
    categories = sorted(set(a) | set(b))
    agree = sum(1 for left, right in zip(a, b) if left == right)
    p_o = agree / n

    count_a = Counter(a)
    count_b = Counter(b)
    p_e = sum((count_a[cat] / n) * (count_b[cat] / n) for cat in categories)
    if p_e == 1.0:
        return 1.0
    return (p_o - p_e) / (1.0 - p_e)


def mean(values: Iterable[float]) -> float:
    data = list(values)
    if not data:
        return 0.0
    return sum(data) / len(data)
