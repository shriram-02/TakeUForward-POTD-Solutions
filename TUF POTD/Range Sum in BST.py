
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (root == nullptr)
            return 0;

        if (root->data < low)
            return rangeSumBST(root->right, low, high);

        if (root->data > high)
            return rangeSumBST(root->left, low, high);

        return root->data
             + rangeSumBST(root->left, low, high)
             + rangeSumBST(root->right, low, high);
    }
};
