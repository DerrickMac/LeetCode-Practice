def search2d(matrix, target):
    # use binary search on the arrays to find which array may contain target

    # l_arr, r_arr = 0, len(matrix) - 1
    l_arr, r_arr = 0, len(matrix) - 1


    while l_arr <= r_arr:
        
        # find the middle array and check if the first value is >, <, == to target
        mid_arr = (r_arr + l_arr) // 2        
        mid_arr_first_val = matrix[mid_arr][0]
        before_mid_first_val = None
        after_mid_first_val = None

        if mid_arr + 1 < len(matrix):
            after_mid_first_val = matrix[mid_arr + 1][0]
        
        if mid_arr - 1 >= 0:
            before_mid_first_val = matrix[mid_arr - 1][0]

        # when l_arr and r_arr are equal, then we have found the array that contains target.
        if l_arr == r_arr:
            break
        
        # if value is greater, then l_arr becomes mid + 1
        elif mid_arr_first_val > target:

            # this checks if target is located in the array before mid
            if before_mid_first_val and before_mid_first_val < target:
                l_arr = mid_arr - 1
                break
            r_arr = mid_arr - 1

        # if value is lesser, then r_arr becomes mid - 1
        elif mid_arr_first_val < target:

            # this checks if target is located in the array after mid
            if after_mid_first_val and after_mid_first_val > target:
                l_arr = mid_arr
                break
            l_arr = mid_arr + 1
        
        else:
            # in case target lies in first val of mid array
            if mid_arr_first_val == target:
                return True
            
            # found target array to do bin search for the target val
            l_arr = mid_arr
            break

    # use normal bin search to find the target within the array
    l, r = 0, len(matrix[l_arr]) - 1

    while l <= r:
        mid_ind = (r + l) // 2
        mid_num = matrix[l_arr][mid_ind]

        # if larger mid_num, then discard mid index and everything else greater
        if mid_num > target:
            r = mid_ind - 1

        # if smaller mid_num, then discard mid index and everything else lesser
        elif mid_num < target:
            l = mid_ind + 1
        
        else:
            # return True if target is in array
            return True

    # return False if target is not in array
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search2d(matrix, target))

# Solution 2
# ROWS, COLS = len(matrix), len(matrix[0])

#     top, bot = 0, ROWS - 1
#     while top <= bot:
#         row = (top + bot) // 2
#         if target > matrix[row][-1]:
#             top = row + 1
#         elif target < matrix[row][0]:
#             bot = row - 1
#         else:
#             break

#     if not (top <= bot):
#         return False
#     row = (top + bot) // 2
#     l, r = 0, COLS - 1
#     while l <= r:
#         m = (l + r) // 2
#         if target > matrix[row][m]:
#             l = m + 1
#         elif target < matrix[row][m]:
#             r = m - 1
#         else:
#             return True
#     return False

