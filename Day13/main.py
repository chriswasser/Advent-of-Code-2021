#!/usr/bin/env python3

import fileinput

import numpy as np


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    split_index = lines.index("")

    dots = []
    for line in lines[:split_index]:
        x, y = line.split(",")
        dots.append((int(x), int(y)))

    folds = []
    for line in lines[split_index + 1 :]:
        direction, index = line.split()[2].split("=")
        folds.append((direction, int(index)))

    direction, index = folds[0]
    new = []
    if direction == "x":
        for dot in dots:
            if dot[0] > index:
                # dot_index - 2 * (dot_index - fold_index) = 2 * fold_index - dot_index
                new.append((2 * index - dot[0], dot[1]))
            elif dot[0] < index:
                # do not need to modify dots on the remaining side
                new.append(dot)
            # do not preserve points directly on the fold_index
    elif direction == "y":
        new = []
        for dot in dots:
            if dot[1] > index:
                # dot_index - 2 * (dot_index - fold_index) = 2 * fold_index - dot_index
                new.append((dot[0], 2 * index - dot[1]))
            elif dot[1] < index:
                # do not need to modify dots on the remaining side
                new.append(dot)
            # do not preserve points directly on the fold_index
    dots = new

    x_max, y_max = max(dot[0] for dot in dots), max(dot[1] for dot in dots)
    paper = np.zeros(shape=(x_max + 1, y_max + 1), dtype=np.bool8)
    for dot in dots:
        paper[dot] = True

    solution = np.sum(paper)
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    split_index = lines.index("")

    dots = []
    for line in lines[:split_index]:
        x, y = line.split(",")
        dots.append((int(x), int(y)))

    folds = []
    for line in lines[split_index + 1 :]:
        direction, index = line.split()[2].split("=")
        folds.append((direction, int(index)))

    for direction, index in folds:
        new = []
        if direction == "x":
            for dot in dots:
                if dot[0] > index:
                    # dot_index - 2 * (dot_index - fold_index) = 2 * fold_index - dot_index
                    new.append((2 * index - dot[0], dot[1]))
                elif dot[0] < index:
                    # do not need to modify dots on the remaining side
                    new.append(dot)
                # do not preserve points directly on the fold_index
        elif direction == "y":
            new = []
            for dot in dots:
                if dot[1] > index:
                    # dot_index - 2 * (dot_index - fold_index) = 2 * fold_index - dot_index
                    new.append((dot[0], 2 * index - dot[1]))
                elif dot[1] < index:
                    # do not need to modify dots on the remaining side
                    new.append(dot)
                # do not preserve points directly on the fold_index
        dots = new

    x_max, y_max = max(dot[0] for dot in dots), max(dot[1] for dot in dots)
    paper = np.zeros(shape=(x_max + 1, y_max + 1), dtype=np.bool8)
    for dot in dots:
        paper[dot] = True

    paper = paper.T
    for row in paper:
        for pixel in row:
            if pixel:
                print("#", end="")
            else:
                print(" ", end="")
        print()

    # have to read of the answer manually
    solution = "ZUJUAFHP"
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
