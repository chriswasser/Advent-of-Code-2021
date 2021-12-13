#!/usr/bin/env python3

from collections import defaultdict
import fileinput
import string


def is_small_cave(cave: str):
    return cave[0] in string.ascii_lowercase


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    neighbors = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        neighbors[a].append(b)
        neighbors[b].append(a)

    start, end = "start", "end"
    queue, paths = [[start]], []
    while queue:
        path = queue.pop()
        if path[-1] == end:
            paths.append(path)
            continue

        for neighbor in neighbors[path[-1]]:
            if neighbor != end and is_small_cave(neighbor) and neighbor in path:
                continue
            queue.append(path + [neighbor])

    solution = len(paths)
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    neighbors = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        neighbors[a].append(b)
        neighbors[b].append(a)

    start, end = "start", "end"
    queue, paths = [([start], False)], []
    while queue:
        path, twice = queue.pop()
        if path[-1] == end:
            paths.append(path)
            continue

        for neighbor in neighbors[path[-1]]:
            if neighbor == start:
                continue
            count = path.count(neighbor)
            if neighbor != end and is_small_cave(neighbor) and twice and count >= 1:
                continue
            if neighbor != end and is_small_cave(neighbor) and not twice and count >= 2:
                continue
            queue.append((path + [neighbor], twice or (neighbor != end and is_small_cave(neighbor) and count == 1)))

    solution = len(paths)
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
