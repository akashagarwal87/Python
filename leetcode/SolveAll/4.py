class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i=j=k = 0
        n1=len(nums1)
        n2=len(nums2)
        sortedArr=[0]*(n1+n2)
        while i < n1 and j < n2:
            if nums1[i]<=nums2[j]:
                sortedArr[k]=nums1[i]
                i+=1
            else:
                sortedArr[k]=nums2[j]
                j+=1
            k+=1
        while i < n1:
            sortedArr[k]=nums1[i]
            i+=1
            k+=1
        while j < n2:
            sortedArr[k]=nums2[j]
            j+=1
            k+=1
        n=n1+n2
        mid=(n)//2
        median=0
        if n %2 == 0:
            median=(sortedArr[mid]+sortedArr[mid-1])/2.0
        else:
            median=sortedArr[mid]*1.0
        return median
        
