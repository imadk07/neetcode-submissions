class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        min_cost=[cost[0],cost[1]]
        if  n <=2:
            return min(cost[0],cost[1])
        for i in range(2, n):
            min_cost.append(
                min(
                    min_cost[i-1],min_cost[i-2])+ cost[i]
            )
        return min(min_cost[-1], min_cost[-2])

        # [1,2,1,2,1,0]
        # [1,2,2,4,3,3]
        # [1,2,3,0]
        # [1,2,4,2]
        #[1,100,1,1,1,100,1,1,100,1,]
        #[1,100,2,3,3,103,4,5,104,6,]

