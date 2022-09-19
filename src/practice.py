print ("Hello")

def check_sum(nums,k):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] ==k:
                return print ("output is", i,j)



print (check_sum([2,11,7,5,4],9))

list=[1,2,3,4,5]
print("\nTuple using list:")


