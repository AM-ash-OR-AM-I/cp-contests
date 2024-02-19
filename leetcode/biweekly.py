from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        def bin_search(sorted_num, target, low, high):
            if low > high:
                return -1
            mid = (low + high) // 2
            if sorted_num[mid][1] == target:
                return target
            if sorted_num[mid][1] > target:
                return bin_search(sorted_num, target, low, mid - 1)
            if sorted_num[mid][1] < target:
                return bin_search(sorted_num, target, mid + 1, high)

        max_sum = float("-inf")
        n = len(nums)
        sum_arr = [0] * (n + 1)
        _sum = 0
        for i, x in enumerate(nums):
            _sum += x
            sum_arr[i + 1] = _sum

        occurrences = defaultdict(list)

        for i, x in enumerate(nums):
            occurrences[x].append(i)

        # set_pairs = set()
        sorted_nums = sorted([(i, x) for i, x in enumerate(nums)], key=lambda x: x[1])
        no_subarr = 1
        for ind, x in sorted_nums:
            target1 = bin_search(sorted_nums, x + k, 0, n - 1)
            target2 = bin_search(sorted_nums, x - k, 0, n - 1)

            if target1 != -1:
                max_sum, no_subarr = self.calculate_max_sum(
                    ind,
                    target1,
                    max_sum,
                    no_subarr,
                    sorted_nums,
                    sum_arr,
                    occurrences=occurrences,
                )

            if target2 != -1:
                max_sum, no_subarr = self.calculate_max_sum(
                    ind,
                    target2,
                    max_sum,
                    no_subarr,
                    sorted_nums,
                    sum_arr,
                    occurrences=occurrences,
                )

        return 0 if no_subarr else max_sum

    @staticmethod
    def calculate_max_sum(
        ind, target, max_sum, no_subarr, sorted_nums, sum_arr, occurrences
    ):

        for ind1 in occurrences[target]:
            g_index = max(ind1, ind)
            s_index = min(ind1, ind)
            no_subarr = 0
            cur_sum = sum_arr[g_index + 1] - sum_arr[s_index]
            max_sum = max(cur_sum, max_sum)
            # if cur_sum == max_sum:
            #     print(f"{(x, ind) = }, {(x+k, ind1) = }, {max_sum = }")

        return max_sum, no_subarr
