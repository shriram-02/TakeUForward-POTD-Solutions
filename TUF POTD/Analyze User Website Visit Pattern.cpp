
class Solution {
public:
    vector<string> mostVisitedPattern(vector<string>& username, vector<int>& timestamp, vector<string>& website) {
        int n = username.size();

        map<string, vector<pair<int, string>>> visits;

        for (int i = 0; i < n; i++) {
            visits[username[i]].push_back({timestamp[i], website[i]});
        }

        map<tuple<string, string, string>, set<string>> patterns;

        for (auto& [user, history] : visits) {
            sort(history.begin(), history.end());

            int m = history.size();
            set<tuple<string, string, string>> userPatterns;

            for (int i = 0; i < m; i++) {
                for (int j = i + 1; j < m; j++) {
                    for (int k = j + 1; k < m; k++) {
                        userPatterns.insert({
                            history[i].second,
                            history[j].second,
                            history[k].second
                        });
                    }
                }
            }

            for (const auto& pattern : userPatterns) {
                patterns[pattern].insert(user);
            }
        }

        tuple<string, string, string> best;
        int maxCount = 0;

        for (const auto& [pattern, users] : patterns) {
            if ((int)users.size() > maxCount) {
                maxCount = users.size();
                best = pattern;
            }
        }

        return {get<0>(best), get<1>(best), get<2>(best)};
    }
};
