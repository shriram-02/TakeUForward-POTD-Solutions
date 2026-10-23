class Solution {
public:
    bool isHeap(vector<int>& nums) {
        int n = nums.size();

        for (int i = 0; i < n / 2; i++) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;

            if (left < n && nums[i] > nums[left])
                return false;

            if (right < n && nums[i] > nums[right])
                return false;
        }

        return true;
    }
};