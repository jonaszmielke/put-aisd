#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include "../one-way-list.cpp"

using namespace std;
using namespace chrono;


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
    vector<int> numbers = readNumbers("../datasets/100k.txt");

    OneWayList list;

    auto start = high_resolution_clock::now();
    for (int num : numbers)
    {
        list.insert(num);
    }
    auto end = high_resolution_clock::now();
    auto duration_insert = duration_cast<milliseconds>(end - start);

    start = high_resolution_clock::now();
    for (int num : numbers)
    {
        list.search(num);
    }
    end = high_resolution_clock::now();
    auto duration_search = duration_cast<milliseconds>(end - start);

    start = high_resolution_clock::now();
    list.~OneWayList();
    end = high_resolution_clock::now();
    auto duration_delete = duration_cast<milliseconds>(end - start);

    ofstream outfile("../test_results/lista-results.csv");
    outfile << "Operacja,Czas_ms\n";
    outfile << "Tworzenie," << duration_insert.count() << "\n";
    outfile << "Wyszukiwanie," << duration_search.count() << "\n";
    outfile << "Usuwanie," << duration_delete.count() << "\n";
    outfile.close();

    cout << "Pomiar zakonczony. Wyniki zapisane w wyniki_lista.csv" << endl;

    return 0;
}
