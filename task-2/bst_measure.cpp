#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

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
};

vector<int> readNumbers(const string &filename)
{
    ifstream file(filename);
    vector<int> numbers;
    int num;
    while (file >> num)
    {
        numbers.push_back(num);
    }
    return numbers;
}

int main()
{
    vector<int> numbers = readNumbers("numbers.txt");

    BST tree;

    auto start = high_resolution_clock::now();
    for (int num : numbers)
    {
        tree.insert(num);
    }
    auto end = high_resolution_clock::now();
    auto duration_insert = duration_cast<milliseconds>(end - start);

    start = high_resolution_clock::now();
    for (int num : numbers)
    {
        tree.search(num);
    }
    end = high_resolution_clock::now();
    auto duration_search = duration_cast<milliseconds>(end - start);

    start = high_resolution_clock::now();
    tree.~BST();
    end = high_resolution_clock::now();
    auto duration_delete = duration_cast<milliseconds>(end - start);

    ofstream outfile("wyniki_bst.csv");
    outfile << "Operacja,Czas_ms\n";
    outfile << "Tworzenie," << duration_insert.count() << "\n";
    outfile << "Wyszukiwanie," << duration_search.count() << "\n";
    outfile << "Usuwanie," << duration_delete.count() << "\n";
    outfile.close();

    cout << "Pomiar zakonczony. Wyniki zapisane w wyniki_bst.csv" << endl;

    return 0;
}
