import random

print("Please Insert The Number :")
n = int(input())
nums = []

for i in range(n) :
    num = random.randint(1, 1000)
    if num not in nums :
     nums.append(num)


print(nums)
