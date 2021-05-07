#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or (roman_string is None):
        return (0)
    Rnum = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
    r_str = roman_string
    conversion = [Rnum[i[0]] if Rnum[i[0]] >= Rnum[i[1]] else (-1*Rnum[i[0]])
                  for i in zip(r_str, r_str[1:] + r_str[-1])]
    return (sum(conversion))
