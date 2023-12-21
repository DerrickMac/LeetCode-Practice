import collections

def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    output = []
    q = collections.deque() # contains indices of nums
    l = r = 0

    # run loop while right pointer is still inbounds
    while r < len(nums):
                    
        # before adding r to queue, pop smaller values from q 
        # to maintain descending order
        # q[-1] refers to the last element in the queue, which is the index of the element in nums
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove left pointer from window
        if l > q[0]:
            q.popleft()

        # if window size is equal to k, add max to output
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    
    return output


