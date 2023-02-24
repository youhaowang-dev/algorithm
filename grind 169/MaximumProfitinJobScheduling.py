# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.


# Example 1:
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
# Example 2:
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
# Example 3:
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6

# DFS + memoization + binary search
# time nlogn space n
class MaximumProfitinJobScheduling:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()

        start_times = [job[0] for job in jobs]
        memo = dict()
        return self.get_max_profit(0, start_times, jobs, memo)

    def get_max_profit(self, i, start_times, jobs, memo):
        if i in memo:
            return memo[i]

        if i == len(start_times):
            return 0
        # case 1 dont do next job
        profit1 = self.get_max_profit(i + 1, start_times, jobs, memo)
        # case 2 do the next job
        # [1,2,3],2 => bisect_left:1, bisect: 2
        j = bisect.bisect_left(start_times, jobs[i][1])
        profit2 = jobs[i][2] + self.get_max_profit(j, start_times, jobs, memo)
        max_profit = max(profit1, profit2)

        memo[i] = max_profit
        return max_profit
