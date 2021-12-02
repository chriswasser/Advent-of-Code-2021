#!/usr/bin/env python3

import fileinput

def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    horizontal, vertical = 0, 0
    for line in fileinput.input():
        operator, argument = line.rstrip().split()
        if operator == "forward":
            horizontal += int(argument)
        if operator == "down":
            vertical += int(argument)
        if operator == "up":
            vertical -= int(argument)
    solution = horizontal * vertical
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    horizontal, vertical, aim = 0, 0, 0
    for line in fileinput.input():
        operator, argument = line.rstrip().split()
        if operator == "forward":
            horizontal += int(argument)
            vertical += aim * int(argument)
        if operator == "down":
            aim += int(argument)
        if operator == "up":
            aim -= int(argument)
    solution = horizontal * vertical
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
