class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        # Total ways to place two distinct knights
        total_squares=n*m
        total_ways=total_squares*(total_squares-1)
        attacking_ways=0
        if n>=2 and m>=3:
            attacking_ways+=4*(n-1)*(m-2)
        if n>=3 and m>=2:
            attacking_ways+=4*(n-2)*(m-1)
        return total_ways -attacking_ways 