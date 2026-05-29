#!/usr/bin/env python3
"""Resolve a finite SU(3) lattice parameter sweep task.

This helper is intentionally small and deterministic.  It maps a SLURM array
index to one point in a Cartesian product of beta values and random seeds, and
prints either JSON metadata or shell assignments for an sbatch wrapper.
"""

from __future__ import annotations

import argparse
import json
import shlex
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class SweepPoint:
    task_id: int
    grid_size: int
    beta: float
    seed: int
    beta_index: int
    seed_index: int


def parse_float_list(text: str) -> list[float]:
    values = [part.strip() for part in text.split(",") if part.strip()]
    if not values:
        raise ValueError("at least one beta value is required")
    return [float(value) for value in values]


def parse_int_list(text: str) -> list[int]:
    values = [part.strip() for part in text.split(",") if part.strip()]
    if not values:
        raise ValueError("at least one seed is required")
    return [int(value) for value in values]


def resolve_task(task_id: int, betas: list[float], seeds: list[int]) -> SweepPoint:
    grid_size = len(betas) * len(seeds)
    if task_id < 0 or task_id >= grid_size:
        raise IndexError(f"task_id {task_id} outside sweep range 0..{grid_size - 1}")
    beta_index = task_id // len(seeds)
    seed_index = task_id % len(seeds)
    return SweepPoint(
        task_id=task_id,
        grid_size=grid_size,
        beta=betas[beta_index],
        seed=seeds[seed_index],
        beta_index=beta_index,
        seed_index=seed_index,
    )


def env_output(point: SweepPoint) -> str:
    fields = {
        "QFT_SWEEP_TASK_ID": point.task_id,
        "QFT_SWEEP_GRID_SIZE": point.grid_size,
        "QFT_SWEEP_BETA": repr(point.beta),
        "QFT_SWEEP_SEED": point.seed,
        "QFT_SWEEP_BETA_INDEX": point.beta_index,
        "QFT_SWEEP_SEED_INDEX": point.seed_index,
    }
    return "\n".join(f"{name}={shlex.quote(str(value))}" for name, value in fields.items())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--betas", default="5.7,5.9,6.1")
    parser.add_argument("--seeds", default="631101,631102,631103")
    parser.add_argument("--task-id", type=int, required=True)
    parser.add_argument("--format", choices=("json", "env"), default="json")
    args = parser.parse_args()

    point = resolve_task(args.task_id, parse_float_list(args.betas), parse_int_list(args.seeds))
    if args.format == "json":
        print(json.dumps(asdict(point), sort_keys=True))
    else:
        print(env_output(point))


if __name__ == "__main__":
    main()
