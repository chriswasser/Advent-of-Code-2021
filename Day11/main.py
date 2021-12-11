#!/usr/bin/env python3

import fileinput
import numpy as np


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    energies = np.empty(shape=(10, 10), dtype=np.int64)
    for row, line in enumerate(lines):
        for col, number in enumerate(line):
            energies[row, col] = int(number)

    flashes = 0
    for _ in range(100):
        for row in range(energies.shape[0]):
            for col in range(energies.shape[1]):
                energies[row, col] += 1

        flashed = np.zeros_like(energies, dtype=np.bool8)
        while True:
            changed = False
            for row in range(energies.shape[0]):
                for col in range(energies.shape[1]):
                    if energies[row, col] > 9 and not flashed[row, col]:
                        flashed[row, col] = True
                        changed = True
                        if row > 0:
                            energies[row - 1, col] += 1
                        if row > 0 and col > 0:
                            energies[row - 1, col - 1] += 1
                        if row > 0 and col < energies.shape[1] - 1:
                            energies[row - 1, col + 1] += 1
                        if row < energies.shape[0] - 1:
                            energies[row + 1, col] += 1
                        if row < energies.shape[0] - 1 and col > 0:
                            energies[row + 1, col - 1] += 1
                        if row < energies.shape[0] - 1 and col < energies.shape[1] - 1:
                            energies[row + 1, col + 1] += 1
                        if col > 0:
                            energies[row, col - 1] += 1
                        if col < energies.shape[1] - 1:
                            energies[row, col + 1] += 1
            if not changed:
                break

        for row in range(energies.shape[0]):
            for col in range(energies.shape[1]):
                if flashed[row, col]:
                    energies[row, col] = 0

        flashes += np.sum(flashed)

    solution = flashes
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    energies = np.empty(shape=(10, 10), dtype=np.int64)
    for row, line in enumerate(lines):
        for col, number in enumerate(line):
            energies[row, col] = int(number)

    flashes = 0
    for day in range(10000):
        for row in range(energies.shape[0]):
            for col in range(energies.shape[1]):
                energies[row, col] += 1

        flashed = np.zeros_like(energies, dtype=np.bool8)
        while True:
            changed = False
            for row in range(energies.shape[0]):
                for col in range(energies.shape[1]):
                    if energies[row, col] > 9 and not flashed[row, col]:
                        flashed[row, col] = True
                        changed = True
                        if row > 0:
                            energies[row - 1, col] += 1
                        if row > 0 and col > 0:
                            energies[row - 1, col - 1] += 1
                        if row > 0 and col < energies.shape[1] - 1:
                            energies[row - 1, col + 1] += 1
                        if row < energies.shape[0] - 1:
                            energies[row + 1, col] += 1
                        if row < energies.shape[0] - 1 and col > 0:
                            energies[row + 1, col - 1] += 1
                        if row < energies.shape[0] - 1 and col < energies.shape[1] - 1:
                            energies[row + 1, col + 1] += 1
                        if col > 0:
                            energies[row, col - 1] += 1
                        if col < energies.shape[1] - 1:
                            energies[row, col + 1] += 1
            if not changed:
                break

        for row in range(energies.shape[0]):
            for col in range(energies.shape[1]):
                if flashed[row, col]:
                    energies[row, col] = 0
        
        if np.all(flashed):
            break

    solution = day + 1
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
