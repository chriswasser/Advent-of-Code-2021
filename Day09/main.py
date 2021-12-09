#!/usr/bin/env python3

import fileinput


def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    grid = []
    for line in lines:
        row = [int(number) for number in line]
        grid.append(row)

    risk = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            ok = True
            if i > 0 and grid[i - 1][j] <= grid[i][j]:
                ok = False
            if i < len(grid) - 1 and grid[i + 1][j] <= grid[i][j]:
                ok = False
            if j > 0 and grid[i][j - 1] <= grid[i][j]:
                ok = False
            if j < len(grid[i]) - 1 and grid[i][j + 1] <= grid[i][j]:
                ok = False
            if ok:
                risk += 1 + grid[i][j]

    solution = risk
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    grid = []
    for line in lines:
        row = [int(number) for number in line]
        grid.append(row)

    visited = []
    for row in grid:
        row = [False for _ in row]
        visited.append(row)

    sizes = []
    i, j = 0, 0
    while True:
        queue = set([(i, j)])

        count = 0
        while queue:
            i, j = queue.pop()
            visited[i][j] = True

            if grid[i][j] == 9:
                continue
            count += 1

            if i > 0 and not visited[i - 1][j]:
                queue.add((i - 1, j))
            if i < len(grid) - 1 and not visited[i + 1][j]:
                queue.add((i + 1, j))
            if j > 0 and not visited[i][j - 1]:
                queue.add((i, j - 1))
            if j < len(grid[i]) - 1 and not visited[i][j + 1]:
                queue.add((i, j + 1))
        sizes.append(count)

        found = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    found = True
                    break
            if found:
                break
        if not found:
            break

    largest = list(sorted(sizes))[-3:]
    solution = largest[0] * largest[1] * largest[2]
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
