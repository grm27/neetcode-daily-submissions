class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        
        for passenger in details:
            if int(passenger[11:13]) > 60:
                res += 1
        
        return res