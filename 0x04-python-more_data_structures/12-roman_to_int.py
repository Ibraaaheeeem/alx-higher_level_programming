#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_to_int = {"M": 1000, "D": 500, "C": 100, "L": 50, "X":10, "V":5, "I": 1}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    total = 0
    num = 0
    for r in reversed(roman_string):
        num = roman_to_int[r]
        total += num if total < num * 5 else -num
    return total
