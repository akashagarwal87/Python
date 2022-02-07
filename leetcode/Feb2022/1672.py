class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth=0
        customers=len(accounts)
        for customer in range(customers):
            maxWealth=max(maxWealth,sum(accounts[customer]))
        return maxWealth