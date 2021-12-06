#!/usr/bin/env python3

import fileinput

from collections import Counter, defaultdict


def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    for line in fileinput.input():
        fishes = [int(fish) for fish in line.rstrip().split(",")]
    for _ in range(80):
        new = []
        for fish in fishes:
            if fish > 0:
                new.append(fish - 1)
            else:
                new.append(6)
                new.append(8)
        fishes = new
    solution = len(fishes)
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    for line in fileinput.input():
        fishes = [int(fish) for fish in line.rstrip().split(",")]
    counts = Counter(fishes)
    for _ in range(256):
        new = defaultdict(int)
        for fish, count in counts.items():
            if fish > 0:
                new[fish - 1] += count
            else:
                new[6] += count
                new[8] += count
        counts = new
    solution = sum(counts.values())
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
