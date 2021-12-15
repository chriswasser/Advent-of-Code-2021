#!/usr/bin/env python3

import fileinput

import networkx as nx


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    graph = nx.DiGraph()
    for x, line in enumerate(lines):
        for y, distance in enumerate(line):
            if x > 0:
                graph.add_edge((x, y), (x - 1, y), length=int(distance))
            if x < len(lines) - 1:
                graph.add_edge((x, y), (x + 1, y), length=int(distance))
            if y > 0:
                graph.add_edge((x, y), (x, y - 1), length=int(distance))
            if y < len(lines) - 1:
                graph.add_edge((x, y), (x, y + 1), length=int(distance))
    length = nx.shortest_path_length(graph, source=(0, 0), target=(len(lines) - 1, len(lines) - 1), weight="length")

    solution = length + int(lines[-1][-1]) - int(lines[0][0])
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    full = []
    for i in range(5):
        for line in lines:
            new = []
            for j in range(5):
                for distance in line:
                    dist = int(distance) + i + j
                    if dist > 9:
                        dist -= 9
                    new.append(dist)
            full.append(new)

    graph = nx.DiGraph()
    for x, line in enumerate(full):
        for y, distance in enumerate(line):
            if x > 0:
                graph.add_edge((x, y), (x - 1, y), length=distance)
            if x < len(full) - 1:
                graph.add_edge((x, y), (x + 1, y), length=distance)
            if y > 0:
                graph.add_edge((x, y), (x, y - 1), length=distance)
            if y < len(full) - 1:
                graph.add_edge((x, y), (x, y + 1), length=distance)
    length = nx.shortest_path_length(graph, source=(0, 0), target=(len(full) - 1, len(full) - 1), weight="length")

    solution = length + full[-1][-1] - full[0][0]
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
