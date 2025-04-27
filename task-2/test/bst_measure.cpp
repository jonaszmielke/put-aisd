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
    vector<int> numbers;
    int num;
    while (file >> num)
    {
        /*cout << num << endl;*/
        numbers.push_back(num);
    }
    return numbers;
}


int main()
{
    vector<int> numbers = readNumbers("../datasets/100k.txt");

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

    ofstream outfile("../test_results/bst_results.csv");
    outfile << "Operacja,Czas_ms\n";
    outfile << "Tworzenie," << duration_insert.count() << "\n";
    outfile << "Wyszukiwanie," << duration_search.count() << "\n";
    outfile << "Usuwanie," << duration_delete.count() << "\n";
    outfile.close();

    cout << "Pomiar zakonczony. Wyniki zapisane w wyniki_bst.csv" << endl;

    return 0;
}
