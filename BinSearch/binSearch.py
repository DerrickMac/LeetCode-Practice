def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid_ind = (r + l) // 2
        mid_num = nums[mid_ind]

        # if larger mid_num, then discard mid index and everything else greater
        if mid_num > target:
            r = mid_ind - 1

        # if smaller mid_num, then discard mid index and everything else lesser
        elif mid_num < target:
            l = mid_ind + 1
        
        else:
            return mid_ind
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))