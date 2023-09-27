def findMin(nums):
    l, r = 0, len(nums) - 1
    result = nums[0]

    while l <= r:
        # case where subarray is already sorted, update result with the minimum of the current result and left pointer
        if nums[l] < nums[r]:
            result = min(result, nums[l])
            break
        
        # use a version of binary search to find if the middle value is part of the left sorted or right sorted part of the array
        mid_ind = (l + r) // 2
        result = min(result, nums[mid_ind])

        # Case of left sorted
        if nums[mid_ind] >= nums[l]:
            l = mid_ind + 1
        
        # case of right sorted
        else:
            r = mid_ind - 1
    
    return result
