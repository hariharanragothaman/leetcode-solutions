class Solution:
    def isRobotBounded(self, s: str) -> bool:
        """
        start = (0, 0) --> (x, y)
        2D place
        L means...
            whatever G after it
        R means..

        Starting at the origin and face north (0,1),
        after one sequence of instructions,

        if chopper return to the origin, he is obvious in an circle.
        if chopper finishes with face not towards north,
        it will get back to the initial status in another one or three sequences.
        """
        x, y, dx, dy = 0, 0, 0, 1
        # smart usage of dx, dy to change directions. Fantastic!
        for c in s:
            if c == "R":
                # remember this is python style in-place comparison
                dx, dy = dy, -dx
            if c == "L":
                dx, dy = -dy, dx
            if c == "G":
                x += dx
                y += dy

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)


if __name__ == "__main__":
    instructions = "GGLLGG"
    instructions = input()
    s = Solution()
    result = s.isRobotBounded(instructions)
    print(f"Is the robot bounded? {result}")
