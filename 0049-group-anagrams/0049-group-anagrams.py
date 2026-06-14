from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        result = []
        anagram_map = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagram_map[key].append(s)

        for value in anagram_map.values():
            result.append(value)
        
        return result   #OR return list(anagram_map.values())
