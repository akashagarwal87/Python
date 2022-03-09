class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArray = [0] * (len(nums1)+len(nums2))
        i = j = k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                sortedArray[k] = nums1[i]
                i += 1
            else:
                sortedArray[k] = nums2[j]
                j += 1
            k += 1
        while i < len(nums1):
            sortedArray[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            sortedArray[k] = nums2[j]
            j += 1
            k += 1
        n = len(sortedArray)
        mid = n//2
        print(sortedArray)
        if n % 2 == 0:
            ans = float(sortedArray[mid-1] + sortedArray[mid])
            print(ans)
            return ans/2
        else:
            return sortedArray[mid]