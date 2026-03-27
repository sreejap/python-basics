# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left+right) // 2
            if isBadVersion (mid):
                # include the right one
                right = mid
            else:
                left = mid + 1 # we don't need it, so discard mid
        
        return left
