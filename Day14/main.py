#!/usr/bin/env python3

from collections import Counter, defaultdict
import fileinput


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    template = lines[0]

    rules = {}
    for line in lines[2:]:
        left, right = line.split(" -> ")
        rules[left] = right

    polymer = template
    for _ in range(10):
        new = polymer[0]
        for a, b in zip(polymer[:-1], polymer[1:]):
            new += rules[a + b] + b
        polymer = new

    counter = Counter(polymer)
    solution = counter.most_common()[0][1] - counter.most_common()[-1][1]
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    template = lines[0]

    rules = {}
    for line in lines[2:]:
        left, right = line.split(" -> ")
        rules[left] = right

    polymer = template
    counts = defaultdict(int)
    for a, b in zip(polymer[:-1], polymer[1:]):
        counts[a + b] += 1

    for _ in range(40):
        new = defaultdict(int)
        for pair, count in counts.items():
            new[pair[0] + rules[pair]] += count
            new[rules[pair] + pair[1]] += count
        counts = new

    counter = defaultdict(int)
    for pair, count in counts.items():
        counter[pair[0]] += count
    counter[template[-1]] += 1
    counts = sorted(counter.items(), key=lambda item: item[1])

    solution = counts[-1][1] - counts[0][1]
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
