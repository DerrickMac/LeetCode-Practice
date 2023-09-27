def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        
        mid_ind = (l + r) // 2
        mid_val = nums[mid_ind]

        if target == mid_val:
            return mid_ind
        
        # left sorted portion
        if mid_val >= nums[l]:
            if target > mid_val or target < nums[l]: # [3, 4, 5, 1, 2] target = 1
                l = mid_ind + 1
            else:
                r = mid_ind - 1
        
        # right sorted portion
        else:
            if target < nums[mid_ind] or target > nums[r]:
                r = mid_ind - 1
            else:
                l = mid_ind + 1

    return -1
