class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for st in strs:
                if i == len(st) or st[i]!=strs[0][i]:
                    return prefix
            prefix+=strs[0][i]
        return prefix
