class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n,m = len(s),len(t)
        count = {letter:0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
        if(n!=m):
            return False
        for i in s:
            count[i]+=1
        for j in t:
            count[j]-=1
        return all(value == 0 for value in count.values())