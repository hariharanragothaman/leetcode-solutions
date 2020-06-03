"""
Given 2 arrays - find the median of 2 sorted arrays.
Here are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

"""
def median_sorted_arrays(nums1, nums2):
    values = sorted(nums1+nums2)
    length = len(values)
    index = length//2

    if length %2 != 0:
        return values[index]
    else:
        return (values[index]+ values[index-1]) / 2.0