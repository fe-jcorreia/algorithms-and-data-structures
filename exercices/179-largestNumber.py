from functools import cmp_to_key

def compare(n1, n2):
  if n1 + n2 > n2 + n1:
    return -1
  else:
    return 1

def largestNumber(nums):
  for i, num in enumerate(nums):
    nums[i] = str(num)

  string = sorted(nums, key=cmp_to_key(compare))

  return str(int("".join(string)))

print(largestNumber([10,2]))
print(largestNumber([3,30,34,5,9]))
print(largestNumber([34323,3432]))