#!/usr/bin/env python3

import fileinput

import numpy as np


def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    for line in fileinput.input():
        positions = np.array([int(position) for position in line.rstrip().split(",")], dtype=np.int64)

    min_fuel = np.sum(positions)
    for alignment in range(max(positions)):
        fuel = np.sum(np.abs(alignment - positions))
        min_fuel = min(fuel, min_fuel)
    solution = min_fuel
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    for line in fileinput.input():
        positions = np.array([int(position) for position in line.rstrip().split(",")], dtype=np.int64)

    min_fuel = np.sum(positions * (positions + 1) // 2)
    for alignment in range(max(positions)):
        diffs = np.abs(alignment - positions)
        fuel = np.sum(diffs * (diffs + 1) // 2)
        min_fuel = min(fuel, min_fuel)
    solution = min_fuel
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
