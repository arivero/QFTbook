#!/usr/bin/env python3
"""Independent checks for the SU(3) cluster sweep grid resolver."""

from __future__ import annotations

import importlib.util
import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
GRID_PATH = ROOT / "qft_scripts" / "cluster" / "su3_sweep_grid.py"


def load_grid_module():
    spec = importlib.util.spec_from_file_location("su3_sweep_grid", GRID_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load su3_sweep_grid.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def check_cartesian_order() -> None:
    grid = load_grid_module()
    betas = [5.7, 5.9, 6.1]
    seeds = [11, 13]
    expected = [
        (0, 5.7, 11, 0, 0),
        (1, 5.7, 13, 0, 1),
        (2, 5.9, 11, 1, 0),
        (3, 5.9, 13, 1, 1),
        (4, 6.1, 11, 2, 0),
        (5, 6.1, 13, 2, 1),
    ]
    for task_id, beta, seed, beta_index, seed_index in expected:
        point = grid.resolve_task(task_id, betas, seeds)
        assert point.grid_size == 6
        assert point.beta == beta
        assert point.seed == seed
        assert point.beta_index == beta_index
        assert point.seed_index == seed_index


def check_bounds() -> None:
    grid = load_grid_module()
    try:
        grid.resolve_task(4, [5.7, 5.9], [11, 13])
    except IndexError:
        return
    raise AssertionError("out-of-range task id was not rejected")


def check_env_cli() -> None:
    proc = subprocess.run(
        [
            sys.executable,
            str(GRID_PATH),
            "--betas",
            "5.7,5.9",
            "--seeds",
            "11,13",
            "--task-id",
            "3",
            "--format",
            "env",
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    fields = dict(line.split("=", 1) for line in proc.stdout.strip().splitlines())
    assert fields["QFT_SWEEP_TASK_ID"] == "3"
    assert fields["QFT_SWEEP_GRID_SIZE"] == "4"
    assert fields["QFT_SWEEP_BETA"] == "5.9"
    assert fields["QFT_SWEEP_SEED"] == "13"
    assert fields["QFT_SWEEP_BETA_INDEX"] == "1"
    assert fields["QFT_SWEEP_SEED_INDEX"] == "1"


def main() -> None:
    check_cartesian_order()
    check_bounds()
    check_env_cli()
    print("All cluster sweep-grid checks passed.")


if __name__ == "__main__":
    main()
