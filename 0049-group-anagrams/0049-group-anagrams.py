from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        result = []
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_strings = tuple(sorted(s))
            anagram_map[sorted_strings].append(s)

        for value in anagram_map.values():
            result.append(value)
        
        return result
