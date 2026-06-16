class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Brute force approach: sort then count until you can't;
        # Hashmap approach: a key for each member of the list.
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest