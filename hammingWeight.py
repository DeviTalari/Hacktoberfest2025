class Solution:
    def hammingWeight(self, n: int) -> int:
        b=str(bin(n))
        count =0
        for i in range(len(b)):
            if b[i]=='1':
                count+=1
        return count

        
