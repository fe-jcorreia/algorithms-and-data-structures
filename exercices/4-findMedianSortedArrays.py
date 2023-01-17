# time: O(n + m) space: O(n + m)
def findMedianSortedArrays(nums1, nums2):
  merged_array = []
  m = len(nums1)
  n = len(nums2)
  merged_len = ((m + n) // 2) + 1
  
  while len(merged_array) != merged_len:
    if len(nums1) == 0:
      merged_array.append(nums2.pop())
      continue

    if len(nums2) == 0:
      merged_array.append(nums1.pop())
      continue

    if nums1[-1] >= nums2[-1]:
      merged_array.append(nums1.pop())
    else:
      merged_array.append(nums2.pop())

  if (m + n) % 2 == 0:
    return (merged_array[-1] + merged_array[-2]) / 2
  else:
    return merged_array[-1]

# time: O(log(n + m)) space: O(n)
def findMedianSortedArrays_opt(nums1, nums2):
  A, B = nums1, nums2
  total = len(nums1) + len(nums2)
  half = total // 2

  if len(B) < len(A):
    A, B = B, A
  
  l, r = 0, len(A) - 1

  while True:
    i = (l + r) // 2
    j = half - i - 2

    Aleft = A[i] if i >= 0 else float("-infinity")
    Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
    Bleft = B[j] if j >= 0 else float("-infinity")
    Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

    if Aleft <= Bright and Bleft <= Aright:
      if total % 2:
        return min(Aright, Bright)
      return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
    elif Aleft > Bright:
      r = i - 1
    else:
      l = i + 1

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))

print(findMedianSortedArrays_opt([1,3], [2]))
print(findMedianSortedArrays_opt([1,2], [3,4]))
