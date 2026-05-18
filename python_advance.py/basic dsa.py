#Sum of List Elements

def sum_of_list(nums):
    total=0
    for num in nums:
        total+=num
    return total

print(sum_of_list([1,2,3]))

#Largest Element
def largest_element(nums):
    max_num=nums[0]
    for num in nums:
        if num>max_num:
            max_num=num
    return largest_element

# Remove Duplicates
def remove_duplicates(nums):
    return list(set(nums))


# Check if All Unique
def unique(nums):
    return nums==set[nums]

#def count_odd_even(nums):
    odd = 0
    even = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return {"odd": odd, "even": even}


#max diff
def max_consecutive_diff(nums):
    max_diff = 0
    for i in range(len(nums)-1):
        diff = abs(nums[i+1] - nums[i])
        if diff > max_diff:
            max_diff = diff
    return max_diff