class Solution:
    def maxSubstring(self, s):
        # code here
        if '0' not in s:
            return -1
        curr=0
        ans=0
        for ch in s:
            if ch=='0':
                curr+=1
            else:
                curr-=1
            if curr<0:
                curr=0
            ans=max(ans,curr)
        return ans