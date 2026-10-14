nums = []
for i in range(14, 56):
    nums.append(i)

print(nums)

#exceto no 25, sobrescreva nos demais pela letra a.

for i in range(len(nums)):
    if nums[i] == 25:
        continue
    nums[i] = 'a'