class Solution:
    def totalMoney(self, n: int) -> int:
        """
        1 2 3 4 5 6 7   7    Week 0 ..
        2 3 4 5 6 7 8  14    Week 1 ... 1
        3 4 5 6 7 8 9  21    Week 2 ... 1, 2

        Week n --  n missing and start from n + 1
        nth week will have
        and so on....

        4 / 7  = 0    This will give the week...
        11 / 7 = 1
        17 / 7 = 2

        remainder = 3
                    4
                    3

        From that number, we can get -- Week+1 * 7 = will give the max_limit
        max_limit - the day will give the index-limit to which we have to calculate

        """
        if n < 7:
            return (n * (n + 1)) // 2

        else:
            weeks_completed = n // 7
            print(f"Weeks completed is {weeks_completed}")

            max_days_in_current_week = (weeks_completed + 1) * 7
            print(f"Max days in current week: {max_days_in_current_week}")

            remaining_days = n - (weeks_completed * 7)
            print(f"Remaining days {remaining_days}")

            # Calculating for previous weeks...
            org = 7
            total = 0
            for i in range(weeks_completed):
                total += sum(range(1, org + 1)) - sum(range(0, i + 1))
                org += 1

            # Calculating for current week...
            j = weeks_completed + 1
            rem = sum(range(j, j + remaining_days))
            total += rem
            return total
