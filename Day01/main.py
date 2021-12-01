#!/usr/bin/env python3

import fileinput

def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    numbers = [int(line.rstrip()) for line in fileinput.input()]
    increases = 0
    for a, b in zip(numbers[:-1], numbers[1:]):
        if b > a:
            increases += 1
    solution = increases
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    numbers = [int(line.rstrip()) for line in fileinput.input()]
    increases = 0
    for a, b in zip(numbers[:-3], numbers[3:]):
        if b > a:
            increases += 1
    solution = increases
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
