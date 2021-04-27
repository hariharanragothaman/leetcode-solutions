"""
Given an array of points, find the number of closest points to origin
"""

from typing import List
import heapq


def KClosest_using_sort(points: List[List[int]], k: int) -> List[List[int]]:
    points = sorted(points, lambda P: P[0] ** 2 + P[1] ** 2)
    return points[:k]


def KClosest_using_heap(points: List[List[int]], k: int) -> List[List[int]]:
    return heapq.nsmallest(k, points, key=lambda P: P[0] ** 2 + P[1] ** 2)
