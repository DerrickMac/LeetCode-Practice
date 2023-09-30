# Binary Search Method


def findMedianSortedARrays(nums1, nums2):
    
    a, b = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # ensure that the smaller arrau is set to varaible 'a'.
    if len(b) < len(a):
        a, b = b, a
    
    l, r = 0, len(a) - 1
    
    # since these two sorted arrays are guaranteed a median, we can set this generic while condition
    while True:
        
        # compute middle value of array a
        a_p = (l + r) // 2
        
        # computer middle value of array b
        b_p = half - a_p - 2

        a_left = a[a_p] if a_p >= 0 else float("-infinity")
        a_right = a[a_p + 1] if (a_p + 1) < len(a) else float("infinity")
        b_left = b[b_p] if b_p >= 0 else float("-infinity")
        b_right = b[b_p + 1] if (b_p + 1) < len(b) else float("infinity")

        if a_left <= b_right and b_left <= a_right:
            
            # odd
            if total % 2:
                return min(a_right, b_right)
            return max(a_left, b_left) + min(a_right, b_right) / 2

        elif a_left > b_right:
            r = a_p - 1
        
        else:
            l = a_p + 1

# Brute Force Method

def findMedianSortedArrays(self, nums1, nums2):
        # Merge the arrays into a single sorted array.
        merged = nums1 + nums2

        # Sort the merged array.
        merged.sort()

        # Calculate the total number of elements in the merged array.
        total = len(merged)

        if total % 2 == 1:
            # If the total number of elements is odd, return the middle element as the median.
            return float(merged[total // 2])
        else:
            # If the total number of elements is even, calculate the average of the two middle elements as the median.
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0
        

# Two pointer method
def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0

        # Find median.
        for count in range(0, (n + m) // 2 + 1):
            m2 = m1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1

        # Check if the sum of n and m is odd.
        if (n + m) % 2 == 1:
            return float(m1)
        else:
            ans = float(m1) + float(m2)
            return ans / 2.0