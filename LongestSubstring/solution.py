class Solution:
    def lengthofLongestSubstring(self,s:str)->int:
        # 2 pointer sliding window method
        maxi = 0
        l = 0
        dmap = []
        for r in range(len(s)):
            if s[r] in dmap:
                while l<r and s[r] in dmap:
                    dmap.remove(s[l])
                    l+=1
            dmap.append(s[r])
            maxi = max(maxi,r-l+1)
        return maxi
    

x = Solution().lengthofLongestSubstring("abcabcbbc")
print(x)
y = Solution().lengthofLongestSubstring("bbbbb")
print(y)
z = Solution().lengthofLongestSubstring("pwwkew")
print(z)
