class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)

        l = l1+l2
        if l%2 = 1:
        	return self.kth(nums1, nums2, l//2)
        else:
        	return (self.kth(nums1, nums2, l//2) + self.kth(nums1, nums2, l//2-1))

        	
        kth(nums1, nums2, l)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
    
    def kth(A, B, k):

    	if not A:
    		return B[k]
    	if not B:
    		return A[k]

    	indexA, indexB = len(A) //2, len(B)//2
    	midA, midB = a[indexA], b[indexB]

    	if k > indexA +indexB:

    		if midA > midB:
    			return self.kth(a, b[indexB+1:], k-indexB-1)
    		else:
    			return self.kth(a[indexA+1:], b, k-indexA-1)
    	else:

    		if midA > midB:
    			return self.kth(a[:indexA], b, k)
    		else:
    			return self.kth(a, b[:indexB], k)
