
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        string A, B;
        cin >> A >> B;

        if (A.length() != B.length()) {
            cout << "NO" << endl;
            continue;
        }

        int freq[26] = {0};

        // Count characters in A
        for (char ch : A) {
            freq[ch - 'a']++;
        }

        // Subtract characters in B
        for (char ch : B) {
            freq[ch - 'a']--;
        }

        bool isAnagram = true;

        // Check frequency array
        for (int i = 0; i < 26; i++) {
            if (freq[i] != 0) {
                isAnagram = false;
                break;
            }
        }

        cout << (isAnagram ? "YES" : "NO") << endl;
    }

    return 0;
}
