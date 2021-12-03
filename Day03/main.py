#!/usr/bin/env python3

from collections import defaultdict
import fileinput


def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    numbers = [line.rstrip() for line in fileinput.input()]

    zeros, ones = defaultdict(int), defaultdict(int)
    for number in numbers:
        for index, digit in enumerate(number):
            if digit == '0':
                zeros[index] += 1
            elif digit == '1':
                ones[index] += 1

    gamma, epsilon = "", ""
    for index in range(len(numbers[0])):
        if zeros[index] > ones[index]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    solution = int(gamma, base=2) * int(epsilon, base=2)
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    numbers = [line.rstrip() for line in fileinput.input()]

    filtered, index = numbers, 0
    while len(filtered) > 1:
        counts = defaultdict(int)
        for number in filtered:
            counts[number[index]] += 1
        if counts["0"] > counts["1"]:
            filtered = [number for number in filtered if number[index] == "0"]
        else:
            filtered = [number for number in filtered if number[index] == "1"]
        index += 1
    oxygen = filtered[0]

    filtered, index = numbers, 0
    while len(filtered) > 1:
        counts = defaultdict(int)
        for number in filtered:
            counts[number[index]] += 1
        if counts["0"] > counts["1"]:
            filtered = [number for number in filtered if number[index] == "1"]
        else:
            filtered = [number for number in filtered if number[index] == "0"]
        index += 1
    co2 = filtered[0]

    solution = int(oxygen, base=2) * int(co2, base=2)
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
