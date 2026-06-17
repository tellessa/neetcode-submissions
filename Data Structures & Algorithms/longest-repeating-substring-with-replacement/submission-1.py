class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find distance between instances of the same letter.
        # if that distance is equal to k, return k + 2
        # elif that distance is shorter than k, keep replacing but skip more of the same letter.
        # elif that distance is longer than k, consider other letters to replace
        # a dict could track the index of each letter.

        # His solution:
        # slide the window across the string and count how many characters inside it already match c.
        # Once you see there are enough characters that don't match c for it to be impossible
        # to replace them all with only k replacements, shrink window from left.

        # one loop to go through all possible characters in the char set of input string
        # another to move pointer r, stretching window to the right
        # we start at 0 and not 1 because we are checking if the given c of charSet is
        # even here at index 0. this contrasts my intuitive approach which would be
        # to choose whatever is the first char of s, and start checking index 1 and beyond
        # for matches

        # checks for substring length to see how many chars need replacement. 
        # longer than 
        #  while (r - l + 1) - count > k:
        #      we need to dock 1 point if we had been getting one from the left window edge,
        # and squish the window from the left side.
        #      that sacrafice is worth making because it comes with the potential
        #      of extending the count by 2 on the other side.
        #  when we leave the while, we know we have the window size for that r position
        #  compare it with old max, and update max. then move to next r for that c until
        #  full string s has been checked, and move to 
        #  next c after that.

        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
