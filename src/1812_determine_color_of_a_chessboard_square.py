"""
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.



Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

Example 3:

Input: coordinates = "c7"
Output: false



Constraints:

    coordinates.length == 2
    'a' <= coordinates[0] <= 'h'
    '1' <= coordinates[1] <= '8'

"""


class Solution:
    def squareIsWhite(self, c: str) -> bool:
        # black = 0, white = 1
        s1 = 'aceg'
        s2 = 'bdfh'
        hmap = {s1: '01010101', s2: '10101010'}

        c = [k for k in c]
        char, digit = c

        if char in s1:
            string = hmap[s1]
        elif char in s2:
            string = hmap[s2]

        val = string[int(digit) - 1]

        if val == '0':
            return False
        else:
            return True
