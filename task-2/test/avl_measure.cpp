#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include "../bst.cpp"

using namespace std;
using namespace chrono;

vector<int> readNumbers(const string &filename)
{
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "ERROR: could not open data-file: " 
             << filename << "\n";
        return {};
    }
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

    ofstream outfile("../test_results/avl_results.csv");
    outfile << "Ilość elementów,Wysokość BST, Wysokość AVL\n";

    for (int i = 1; i<=20; i++){
        
        vector<int> numbers = readNumbers("../datasets/" + to_string(i) + "k.txt");
    
        BST bst;
        for (int num : numbers)
        {
            bst.insert(num);
        }
    
        int bst_height = bst.height();
        bst.balance();
        int avl_height = bst.height();

        outfile << i << "," << bst_height << "," << avl_height << "\n";
    }

    return 0;
}
