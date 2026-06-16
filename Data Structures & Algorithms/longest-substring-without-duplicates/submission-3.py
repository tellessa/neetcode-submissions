class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize
        seen = set()
        l = 0
        Smax = 0

        # loop
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                # this may be start of new longest substring, so move l here
                l += 1
            # we hadn't seen it yet and now we have.
            seen.add(s[r])
            Smax = max(len(seen), Smax)
            # Smax = max(Smax, r - l + 1)

        # return
        return Smax