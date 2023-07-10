def combine(n, k):
  nums = [i for i in range(1, n + 1)]
  currComb = []
  ans = []

  def dfs(index):
    if len(currComb) == k:
      ans.append(currComb[:])
      return

    for i in range(index, len(nums)):
      currComb.append(nums[i])
      dfs(i + 1)
      currComb.pop()

  dfs(0)
  return ans

def combine_(n, k):
  mp = {}

  def comb(n, k):
    if n == 1 and k == 1:
      mp[(1, 1)] = [[1]]
      return [[1]]
    
    if (n, k) in mp:
      return mp[(n, k)]

    ans = []
    if k == 1:
      ans = [[x] for x in range(1, n + 1)]  # Create a list of single-element combinations
    elif n == k:
      ans = [list(range(1, n + 1))]  # Create a list with a single combination of all elements
    else:
      ans = comb(n - 1, k)  # Get combinations without the last element (n)
      c_wo_n = comb(n - 1, k - 1)  # Get combinations with (k-1) elements from (n-1)
      for v in c_wo_n:
        v_w_n = v + [n]  # Add the last element (n) to each combination
        ans.append(v_w_n)  # Append the extended combinations to the answer list

    mp[(n, k)] = ans

    return ans

  return comb(n, k)

print(combine(4, 2))
print(combine(1, 1))