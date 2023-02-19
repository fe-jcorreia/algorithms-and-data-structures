def merge(nums1, m, nums2, n):
  i = j = 0
  temp = []

  while i != m and j != n:
    if nums2[j] < nums1[i]:
      temp.append(nums2[j])
      j += 1
    else:
      temp.append(nums1[i])
      i += 1

  while i != m:
    temp.append(nums1[i])
    i += 1
  while j != n:
    temp.append(nums2[j])
    j += 1

  i = 0
  for num in temp:
    nums1[i] = num
    i += 1

def merge_opt(nums1, m, nums2, n):
  p1 = m - 1
  p2 = n - 1
  p = m + n - 1

  while p1 >= 0 and p2 >= 0:
    if nums1[p1] > nums2[p2]:
      nums1[p] = nums1[p1]
      p1 -= 1
    else:
      nums1[p] = nums2[p2]
      p2 -= 1
    p -= 1
  
  nums1[:p2 + 1] = nums2[:p2 + 1]
  

# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]

nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]

# merge(nums1, 3, nums2, 3)
merge_opt(nums1, 3, nums2, 3)

print(nums1)