class Solution {
public:
    vector<char> frequencySort(string& s) {
        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++;
        }

        vector<char> ans;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                ans.push_back('a' + i);
            }
        }

        sort(ans.begin(), ans.end(), [&](char a, char b) {
            if (freq[a - 'a'] != freq[b - 'a']) {
                return freq[a - 'a'] > freq[b - 'a'];
            }
            return a < b;
        });

        return ans;
    }
};