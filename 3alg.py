nums = [1000000, 100, 3, 4, 5, 9, 1000, 1001, 10000000000]
max_element = nums[0]

for num in nums:
    if num > max_element:
        max_element = num
print("Наибольшее число: ", max_element)
