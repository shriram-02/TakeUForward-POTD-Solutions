class Solution {
public:
    int maxDepthBST(vector<int>& order) {
        int n = order.size();
        vector<int> depth(n + 1, 0);
        vector<int> parent(n + 1, 0);
        set<int> inserted;
        int ans = 0;

        for (int x : order) {
            auto it = inserted.lower_bound(x);
            int leftDepth = 0, rightDepth = 0;

            if (it != inserted.begin()) {
                auto prevIt = prev(it);
                leftDepth = depth[*prevIt];
            }

            if (it != inserted.end()) {
                rightDepth = depth[*it];
            }

            depth[x] = max(leftDepth, rightDepth) + 1;
            ans = max(ans, depth[x]);
            inserted.insert(x);
        }

        return ans;
    }
};