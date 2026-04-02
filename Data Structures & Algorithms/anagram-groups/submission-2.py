class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            occur = [0]*26
            for char in word:
                occur[ord(char) - ord('a')] += 1

            result[tuple(occur)].append(word)

        return list(result.values())

            
        