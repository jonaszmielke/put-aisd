#include <vector>
#include <algorithm>

class BST
{
private:
    struct Node
    {
        int info;
        Node *left;
        Node *right;
        Node(int x) : info(x), left(nullptr), right(nullptr) {}
    };

    Node *root;

    Node *insert(Node *node, int x)
    {
        if (!node)
            return new Node(x);
        if (x < node->info)
            node->left = insert(node->left, x);
        else if (x > node->info)
            node->right = insert(node->right, x);
        return node;
    }

    Node *search(Node *node, int x) const
    {
        if (!node || node->info == x)
            return node;
        if (x < node->info)
            return search(node->left, x);
        else
            return search(node->right, x);
    }

    void destroy(Node *node)
    {
        if (!node)
            return;
        destroy(node->left);
        destroy(node->right);
        delete node;
    }

    int height(Node *node) const
    {
        if (!node)
            return 0;
        int lh = height(node->left);
        int rh = height(node->right);
        return 1 + std::max(lh, rh);
    }

    std::vector<int> inorderVec(Node *node) const
    {
        std::vector<int> result;
        if (!node)
            return result;
        auto left = inorderVec(node->left);
        result.insert(result.end(), left.begin(), left.end());
        result.push_back(node->info);
        auto right = inorderVec(node->right);
        result.insert(result.end(), right.begin(), right.end());
        return result;
    }

    static Node *buildBalanced(const std::vector<int> &v, int l, int r)
    {
        if (l > r)
            return nullptr;
        int m = (l + r) / 2;
        Node *node = new Node(v[m]);
        node->left = buildBalanced(v, l, m - 1);
        node->right = buildBalanced(v, m + 1, r);
        return node;
    }

public:
    BST() : root(nullptr) {}
    ~BST() { destroy(root); }

    void insert(int x) { root = insert(root, x); }
    bool search(int x) const { return search(root, x) != nullptr; }
    std::vector<int> inorder() const { return inorderVec(root); }
    std::vector<int> preorder() const { /* ... */ return {}; }
    std::vector<int> postorder() const { /* ... */ return {}; }
    int height() const { return height(root); }

    void balance()
    {
        auto v = inorder();
        destroy(root);
        root = buildBalanced(v, 0, v.size() - 1);
    }
};
