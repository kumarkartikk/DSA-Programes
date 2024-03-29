def canReach(self, s, minJ, maxJ):
        dp = [c == '0' for c in s]
        pre = 0
        for i in xrange(1, len(s)):
            if i >= minJ: pre += dp[i - minJ]
            if i > maxJ: pre -= dp[i - maxJ - 1]
            dp[i] &= pre > 0
        return dp[-1]
