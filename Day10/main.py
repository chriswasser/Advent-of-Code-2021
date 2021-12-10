#!/usr/bin/env python3

import fileinput


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    for line in lines:
        stack = []
        for character in line:
            if character in ["(", "[", "{", "<"]:
                stack.append(character)
            if character in [")", "]", "}", ">"]:
                if stack[-1] == close_to_open[character]:
                    stack.pop()
                else:
                    score += points[character]
                    break

    solution = score
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    open_to_close = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores = []
    for line in lines:
        legal = True
        stack = []
        for character in line:
            if character in ["(", "[", "{", "<"]:
                stack.append(character)
            if character in [")", "]", "}", ">"]:
                if stack[-1] == close_to_open[character]:
                    stack.pop()
                else:
                    legal = False
                    break
        if legal and stack:
            score = 0
            for character in reversed(stack):
                score *= 5
                score += points[open_to_close[character]]
            scores.append(score)
    
    solution = sorted(scores)[len(scores) // 2]
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
