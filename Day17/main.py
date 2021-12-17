#!/usr/bin/env python3

import fileinput
import math
import re


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    pattern = re.compile(r"target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)")
    match = pattern.match(lines[0])
    target = [int(group) for group in match.groups()]

    velocities = [(x, y) for x in range(-250, 250) for y in range(-250, 250)]
    reach = []
    for initial in velocities:
        position = (0, 0)
        velocity, max_height = initial, 0
        for _ in range(1000):
            if target[0] <= position[0] <= target[1] and target[2] <= position[1] <= target[3]:
                reach.append((initial, max_height))
                break
            position = position[0] + velocity[0], position[1] + velocity[1]
            velocity = velocity[0] - math.copysign(1, velocity[0]) if velocity[0] != 0 else 0, velocity[1] - 1
            if position[1] > max_height:
                max_height = position[1]

    solution = sorted(reach, key=lambda item: item[1])[-1][1]
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    pattern = re.compile(r"target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)")
    match = pattern.match(lines[0])
    target = [int(group) for group in match.groups()]

    velocities = [(x, y) for x in range(-250, 250) for y in range(-250, 250)]
    reach = []
    for initial in velocities:
        position = (0, 0)
        velocity, max_height = initial, 0
        for _ in range(1000):
            if target[0] <= position[0] <= target[1] and target[2] <= position[1] <= target[3]:
                reach.append((initial, max_height))
                break
            position = position[0] + velocity[0], position[1] + velocity[1]
            velocity = velocity[0] - math.copysign(1, velocity[0]) if velocity[0] != 0 else 0, velocity[1] - 1
            if position[1] > max_height:
                max_height = position[1]

    solution = len(reach)
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
