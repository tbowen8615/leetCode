import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = []

        # Add all numbers in the initial list to the heap
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)

        # Ensure the heap size does not exceed k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The root of the heap is the kth largest element

        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(obj.add(3))  # Output: 4
print(obj.add(5))  # Output: 5
print(obj.add(10)) # Output: 5
print(obj.add(9))  # Output: 8
print(obj.add(4))  # Output: 8
