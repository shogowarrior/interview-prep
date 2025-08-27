# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

import heapq

def kth_largest(nums, k):
    heap = nums[:k]                    # Take first k elements
    heapq.heapify(heap)                # Convert to a min-heap

    for num in nums[k:]:               # Iterate over the rest of the elements
        if num > heap[0]:              # If the current number is larger than the smallest in the heap
            heapq.heappop(heap)        # Remove the smallest
            heapq.heappush(heap, num)  # Insert the current number
    return heap[0]                     # The root of the heap is the kth largest element



nums = [3,2,1,5,6,4]
k = 2
print(kth_largest(nums, k))
## 5

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(kth_largest(nums, k))
## 4
