class Solution {
public:
    int maxProfit(vector<int>& prices, vector<int>& profits) {
        int n = prices.size();
        int ans = -1;

        for (int j = 1; j < n - 1; j++) {
            int left = 0, right = 0;

            for (int i = 0; i < j; i++) {
                if (prices[i] < prices[j]) {
                    left = max(left, profits[i]);
                }
            }

            for (int k = j + 1; k < n; k++) {
                if (prices[j] < prices[k]) {
                    right = max(right, profits[k]);
                }
            }

            if (left > 0 && right > 0) {
                ans = max(ans, left + profits[j] + right);
            }
        }

        return ans;
    }
};