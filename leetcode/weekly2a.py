from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_sum = 0
        for x in nums:
            xor_sum ^= x
        y = xor_sum ^ k
        return bin(y).count('1')