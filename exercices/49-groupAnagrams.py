def groupAnagrams(strs):
  groups = {}

  for string in strs:
    count = [0] * 26

    for char in string:
      count[ord(char) - ord('a')] += 1
    
    if not groups.get(tuple(count)):
      groups[tuple(count)] = [string]
    else:
      groups[tuple(count)].append(string)

  return groups.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# print(groupAnagrams([""]))
# print(groupAnagrams(["a"]))
