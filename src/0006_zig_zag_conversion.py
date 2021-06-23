"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""


def convert(s, number_of_rows):
    if number_of_rows == 1 or number_of_rows > len(s):
        return s

    result = [""] * number_of_rows
    index, step = 0, 1

    for char in s:
        result[index] += char

        if index == 0:
            step = 1
        elif index == number_of_rows - 1:
            step = -1
        index += step

    return "".join(result)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    op = convert(s, 3)
    print(op)
