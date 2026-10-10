class Solution {
public:
    string characterFrequency(const string& s) {
        map<char, int> freq;

        for (char ch : s) {
            freq[ch]++;
        }

        string result = "";
        for (auto& p : freq) {
            result += p.first;
            result += to_string(p.second);
            result += " ";
        }

        if (!result.empty()) {
            result.pop_back();
        }

        return result;
    }
};