class Solution(object):
    def longestPalindrome(self, s):
        temp = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] == s[j:i-1:-1] and j-i+1 > len(temp):
                    temp = s[i:j+1]
        return temp

if __name__ == "__main__":
    sl = Solution()
    print(sl.longestPalindrome("a"))