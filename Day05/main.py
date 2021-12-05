#!/usr/bin/env python3

import fileinput

import numpy as np


def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    vents = np.zeros(shape=(1000, 1000), dtype=np.int64)
    for line in fileinput.input():
        start, end = line.rstrip().split(" -> ")
        start_x, start_y = start.split(",")
        end_x, end_y = end.split(",")

        if start_x != end_x and start_y != end_y:
            continue
        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)

        if start_x > end_x:
            start_x, end_x = end_x, start_x
        if start_y > end_y:
            start_y, end_y = end_y, start_y

        vents[start_x : end_x + 1, start_y : end_y + 1] += 1

    solution = np.count_nonzero(vents >= 2)
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    vents = np.zeros(shape=(1000, 1000), dtype=np.int64)
    for line in fileinput.input():
        start, end = line.rstrip().split(" -> ")
        start_x, start_y = start.split(",")
        end_x, end_y = end.split(",")

        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)

        dir_x = np.sign(end_x - start_x)
        dir_y = np.sign(end_y - start_y)

        factor = 0
        while not (start_x + factor * dir_x == end_x and start_y + factor * dir_y == end_y):
            vents[start_x + factor * dir_x, start_y + factor * dir_y] += 1
            factor += 1
        vents[end_x, end_y] += 1

    solution = np.count_nonzero(vents >= 2)
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
