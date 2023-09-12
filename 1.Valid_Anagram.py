class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #soln 2
        return sorted(s)==sorted(t)

        # soln 1 alternative 
        return Counter(s)==Counter(t)

        # soln 1
        countS, countT ={}, {}

        if len(s)!=len(t):
            return False

        for c in s:
            countS[c]=1+countS.get(c,0)

        for c in t:
            countT[c]=1+countT.get(c,0)

        for val in countS:
            if countS[val]!=countT.get(val,0):
                return False
            
        return True
