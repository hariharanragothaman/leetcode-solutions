from typing import *

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        total = 0
        curr_boxes = 0
        for box_count, units in boxTypes:
            if curr_boxes + box_count <= truckSize:
                total += box_count * units
                curr_boxes += box_count
            else:
                remaining = truckSize - curr_boxes
                total +=  remaining * units
                curr_boxes += remaining
        return total