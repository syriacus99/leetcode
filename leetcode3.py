class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                j = max(j, dic[s[i]]+1)
                dic[s[i]] = i
            res = max(res, i-j+1)
        return res

s = "abcabcbb"
a = Solution()
print(a.lengthOfLongestSubstring(s))

#只遍历一遍，在遍历中调整左框和右框的位置，通过字典存储每个字符最后出现的位置,出现相同的，则左框右移