class Solution {
public:
    void insertAtBottom(stack<int>& st, int x) {
        if (st.empty()) {
            st.push(x);
            return;
        }

        int top = st.top();
        st.pop();
        insertAtBottom(st, x);
        st.push(top);
    }

    void reverseStack(stack<int>& st) {
        if (st.empty()) return;

        int top = st.top();
        st.pop();
        reverseStack(st);
        insertAtBottom(st, top);
    }
};