#!/usr/bin/env python3

import fileinput
import math


def test_task1():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 1: ok")


def parse_packet(versions, packet, index=0):
    version = packet[index : index + 3]
    index += 3

    versions.append(version)

    packet_type = packet[index : index + 3]
    index += 3

    if packet_type == "100":  # literal value
        value = ""
        while True:
            prefix = packet[index]
            index += 1

            if prefix == "1":
                value += packet[index : index + 4]
                index += 4
            elif prefix == "0":
                value += packet[index : index + 4]
                index += 4
                break
    else:
        length_type = packet[index]
        index += 1

        if length_type == "0":  # 15 bits of total length
            total_length = int(packet[index : index + 15], base=2)
            index += 15

            start_index = index
            while start_index != index + total_length:
                start_index = parse_packet(versions, packet, start_index)
            index += total_length
        elif length_type == "1":  # 11 bits of #subpackets
            num_subpackets = int(packet[index : index + 11], base=2)
            index += 11

            for _ in range(num_subpackets):
                index = parse_packet(versions, packet, index)
    return index


def solve_task1():
    lines = [line.rstrip() for line in fileinput.input()]

    num_bits = 4 * len(lines[0])
    packet = bin(int(lines[0], base=16))[2:].zfill(num_bits)
    versions = []
    parse_packet(versions, packet)
    version_sum = sum(int(version, base=2) for version in versions)

    solution = version_sum
    print(f"answer to task 1: {solution}")


def test_task2():
    lines = [line.rstrip() for line in fileinput.input()]
    assert True
    print("tests for task 2: ok")


def parse_packet2(packet, index=0):
    version = packet[index : index + 3]
    index += 3

    packet_type = packet[index : index + 3]
    index += 3

    if packet_type == "100":  # literal value
        value = ""
        while True:
            prefix = packet[index]
            index += 1

            if prefix == "1":
                value += packet[index : index + 4]
                index += 4
            elif prefix == "0":
                value += packet[index : index + 4]
                index += 4
                break
        return int(value, base=2), index
    else:
        length_type = packet[index]
        index += 1

        if length_type == "0":  # 15 bits of total length
            total_length = int(packet[index : index + 15], base=2)
            index += 15

            start_index = index
            values = []
            while start_index != index + total_length:
                value, start_index = parse_packet2(packet, start_index)
                values.append(value)
            index += total_length
        elif length_type == "1":  # 11 bits of #subpackets
            num_subpackets = int(packet[index : index + 11], base=2)
            index += 11

            values = []
            for _ in range(num_subpackets):
                value, index = parse_packet2(packet, index)
                values.append(value)
        if packet_type == "000":
            return sum(values), index
        if packet_type == "001":
            return math.prod(values), index
        if packet_type == "010":
            return min(values), index
        if packet_type == "011":
            return max(values), index
        if packet_type == "101":
            return values[0] > values[1], index
        if packet_type == "110":
            return values[0] < values[1], index
        if packet_type == "111":
            return values[0] == values[1], index


def solve_task2():
    lines = [line.rstrip() for line in fileinput.input()]

    num_bits = 4 * len(lines[0])
    packet = bin(int(lines[0], base=16))[2:].zfill(num_bits)
    value, index = parse_packet2(packet)

    solution = value
    print(f"answer to task 2: {solution}")


def main():
    test_task1()
    solve_task1()
    test_task2()
    solve_task2()


if __name__ == "__main__":
    main()
