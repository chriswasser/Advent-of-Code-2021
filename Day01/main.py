#!/usr/bin/env python3

import fileinput


def num_increases(numbers, offset=1):
    increases = 0
    for a, b in zip(numbers[:-offset], numbers[offset:]):
        if b > a:
            increases += 1
    return increases


def test_task1():
    numbers = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    solution = num_increases(numbers)
    assert solution == 7
    print("tests for task 1: ok")


def solve_task1():
    numbers = [int(line.rstrip()) for line in fileinput.input()]
    solution = num_increases(numbers)
    print(f"answer to task 1: {solution}")


def test_task2():
    numbers = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    solution = num_increases(numbers, offset=3)
    assert solution == 5
    print("tests for task 2: ok")


def solve_task2():
    numbers = [int(line.rstrip()) for line in fileinput.input()]
    solution = num_increases(numbers, offset=3)
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
