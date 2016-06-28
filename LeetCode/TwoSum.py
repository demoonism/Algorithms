def naive(a, b):  # n^2
	for i in range(len(a)):
		for j in range(len(a)):
			if i != j and a[i] + a[j] ==b:
				return i, j


def improve(nums, target): # n^2 amortized. lookup for list is n
	for i in range(len(nums)-1, 0, -1):
		if  target - nums[i] in nums[:i]: #any thing before this has already been tested.
			# very importportant, if going from the same direction, 
			#then index may get the same one as the inital number (nums[i]), 
			#by going backward, it will get a different one
			return nums.index(target - nums[i]), i

def optimize(nums, target): # n, lookup dic is constant.
	if len(nums) < 1:
		return false
	counterpart_dic = {}
	for i in range(len(nums)):
		if nums[i] in counterpart_dic:
			return counterpart_dic[nums[i]], i
		else:
			counterpart_dic[target - nums[i]] = i


nums = [2,7,11,15]
target = 9
#print(naive(nums,target))
print(improve(nums,target))