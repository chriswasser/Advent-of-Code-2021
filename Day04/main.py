#!/usr/bin/env python3

import fileinput
import numpy as np
from numpy.core.fromnumeric import shape

def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    file = fileinput.input()
    numbers = next(file).rstrip().split(",")
    next(file)
    boards, board = [], []
    for line in file:
        line = line.rstrip()
        if not line:
            boards.append(board)
            board = []
        else:
            board.append(line.split())
    boards.append(board)
    
    drawn = np.zeros(shape=(len(boards), len(boards[0]), len(boards[0])), dtype=np.int8)
    for number in numbers:
        for k, board in enumerate(boards):
            for i, line in enumerate(board):
                try:
                    j = line.index(number)
                    drawn[k, i, j] = 1
                except ValueError:
                    pass
        for k, draw in enumerate(drawn):
            for i in range(draw.shape[0]):
                if np.all(draw[i, :] == 1):
                    break
            else:
                for j in range(draw.shape[1]):
                    if np.all(draw[:, j] == 1):
                        break
                else:
                    continue
            break
        else:
            continue
        break

    unmarked = 0
    for i in range(len(boards[k])):
        for j in range(len(boards[k][i])):
            if drawn[k, i, j] == 0:
                unmarked += int(boards[k][i][j])

    solution = unmarked * int(number)
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    file = fileinput.input()
    numbers = next(file).rstrip().split(",")
    next(file)
    boards, board = [], []
    for line in file:
        line = line.rstrip()
        if not line:
            boards.append(board)
            board = []
        else:
            board.append(line.split())
    boards.append(board)

    break_next = False    
    drawn = np.zeros(shape=(len(boards), len(boards[0]), len(boards[0])), dtype=np.int8)
    for index, number in enumerate(numbers):
        for k, board in enumerate(boards):
            for i, line in enumerate(board):
                try:
                    j = line.index(number)
                    drawn[k, i, j] = 1
                except ValueError:
                    pass
        solved = []
        for k, draw in enumerate(drawn):
            for i in range(draw.shape[0]):
                if np.all(draw[i, :] == 1):
                    solved.append(k)
                    break
            else:
                for j in range(draw.shape[1]):
                    if np.all(draw[:, j] == 1):
                        solved.append(k)
                        break
        if break_next and len(solved) == len(boards):
            break
        if len(solved) == len(boards) - 1:
            break_next = True
            last, = set(list(range(len(boards)))).difference(set(solved))
    k = last

    unmarked = 0
    for i in range(len(boards[k])):
        for j in range(len(boards[k][i])):
            if drawn[k, i, j] == 0:
                unmarked += int(boards[k][i][j])

    solution = unmarked * int(number)
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
