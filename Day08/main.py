#!/usr/bin/env python3

from collections import defaultdict
import fileinput


def test_task1():
    assert True
    print("tests for task 1: ok")


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    targets = [2, 3, 4, 7]
    count = 0
    for line in lines:
        digits, output = line.split(" | ")
        count += sum(len(digit) in targets for digit in output.split())

    solution = count
    print(f"answer to task 1: {solution}")


def test_task2():
    assert True
    print("tests for task 2: ok")


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    letters_to_numbers = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }
    outputs = []
    for line in lines:
        digits, output = line.split(" | ")

        counts_all = defaultdict(int)
        for digit in digits.split():
            for letter in digit:
                counts_all[letter] += 1

        selection = [2, 3, 4, 7]
        counts_selection = defaultdict(int)
        for digit in digits.split():
            if len(digit) in selection:
                for letter in digit:
                    counts_selection[letter] += 1

        mapping = {}
        mapping[
            set([letter for letter, count in counts_all.items() if count == 8])
            .intersection(set([letter for letter, count in counts_selection.items() if count == 2]))
            .pop()
        ] = "a"
        mapping[[letter for letter, count in counts_all.items() if count == 6][0]] = "b"
        mapping[
            set([letter for letter, count in counts_all.items() if count == 8])
            .intersection(set([letter for letter, count in counts_selection.items() if count == 4]))
            .pop()
        ] = "c"
        mapping[
            set([letter for letter, count in counts_all.items() if count == 7])
            .intersection(set([letter for letter, count in counts_selection.items() if count == 2]))
            .pop()
        ] = "d"
        mapping[[letter for letter, count in counts_all.items() if count == 4][0]] = "e"
        mapping[[letter for letter, count in counts_all.items() if count == 9][0]] = "f"
        mapping[
            set([letter for letter, count in counts_all.items() if count == 7])
            .intersection(set([letter for letter, count in counts_selection.items() if count == 1]))
            .pop()
        ] = "g"

        output_string = ""
        for digit in output.split():
            result = ""
            for letter in digit:
                result += mapping[letter]
            output_string += letters_to_numbers["".join(sorted(result))]
        outputs.append(int(output_string))

    solution = sum(outputs)
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
