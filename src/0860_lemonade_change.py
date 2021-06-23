"""
At a lemonade stand, each lemonade costs $5.

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.



Example 1:

Input: [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: [5,5,10]
Output: true

Example 3:

Input: [10,10]
Output: false

Example 4:

Input: [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.


"""

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash, cost, hmap = 0, 5, {5: 0, 10: 0, 20: 0}

        for i, c in enumerate(bills):
            if c == cost:
                hmap[c] += 1

            elif c > cost:
                change = c - cost
                hmap = {
                    k: v
                    for k, v in sorted(hmap.items(), key=lambda x: x[0], reverse=True)
                }

                for k, v in hmap.items():
                    if change and v > 0:
                        q, r = divmod(change, k)
                        min_take = min(v, q)
                        hmap[k] -= min_take
                        change -= min_take * k

                if change == 0:
                    hmap[c] += 1
                else:
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
