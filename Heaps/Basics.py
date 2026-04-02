nums = [1,2,3,4,5]
heapq.heapify(nums) # this is min heap

# to get max heap

nums = [-x for x in nums]
heapq.heapify(nums)
