#include <iostream>

using namespace std;

//Binary Search Tree
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
        {
            return new Node(x);
        }
        if (x < node->info)
        {
            node->left = insert(node->left, x);
        }
        else if (x > node->info)
        {
            node->right = insert(node->right, x);
        }
        // jeśli x == node->info, nie wstawiamy duplikatu
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

    // Przechodzenie inorder (LVR LKP)
    void inorder(Node *node) const
    {
        if (!node)
            return;
        inorder(node->left);
        cout << node->info << ' ';
        inorder(node->right);
    }

    // Przechodzenie preorder (VLR KLP)
    void preorder(Node *node) const
    {
        if (!node)
            return;
        cout << node->info << ' ';
        preorder(node->left);
        preorder(node->right);
    }

    // Przechodzenie postorder (LRV LPK)
    void postorder(Node *node) const
    {
        if (!node)
            return;
        postorder(node->left);
        postorder(node->right);
        cout << node->info << ' ';
    }

    void destroy(Node *node)
    {
        if (!node)
            return;
        destroy(node->left);
        destroy(node->right);
        delete node;
    }

public:
    BST() : root(nullptr) {}
    ~BST()
    {
        destroy(root);
    }

    void insert(int x)
    {
        root = insert(root, x);
    }

    bool search(int x) const
    {
        return search(root, x) != nullptr;
    }

    void inorder() const
    {
        inorder(root);
        cout << '\n';
    }

    void preorder() const
    {
        preorder(root);
        cout << '\n';
    }

    void postorder() const
    {
        postorder(root);
        cout << '\n';
    }
};

int main()
{
    BST tree;

    int values[] = {50, 30, 70, 20, 40, 60, 80};
    for (int v : values)
    {
        tree.insert(v);
    }

    cout << "Inorder: ";
    tree.inorder(); // 20 30 40 50 60 70 80

    cout << "Preorder: ";
    tree.preorder(); // 50 30 20 40 70 60 80

    cout << "Postorder: ";
    tree.postorder(); // 20 40 30 60 80 70 50

    // Wyszukiwanie
    int key = 60;
    cout << "Wyszukiwanie " << key << ": " << (tree.search(key) ? "znaleziono\n" : "nie znaleziono\n");

    key = 25;
    cout << "Wyszukiwanie " << key << ": " << (tree.search(key) ? "znaleziono\n" : "nie znaleziono\n");

    return 0;
}