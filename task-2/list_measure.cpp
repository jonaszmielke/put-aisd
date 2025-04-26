#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

struct ListNode
{
    int info;
    ListNode *next;
    ListNode(int x) : info(x), next(nullptr) {}
};

class SortedList
{
private:
    ListNode *head;

public:
    SortedList() : head(nullptr) {}

    ~SortedList()
    {
        while (head)
        {
            ListNode *tmp = head;
            head = head->next;
            delete tmp;
        }
    }

    void insert(int x)
    {
        ListNode *newNode = new ListNode(x);
        if (!head || head->info > x)
        {
            newNode->next = head;
            head = newNode;
            return;
        }
        ListNode *current = head;
        while (current->next && current->next->info < x)
        {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }

    bool search(int x)
    {
        ListNode *current = head;
        while (current)
        {
            if (current->info == x)
                return true;
            current = current->next;
        }
        return false;
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

    SortedList list;

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
    list.~SortedList();
    end = high_resolution_clock::now();
    auto duration_delete = duration_cast<milliseconds>(end - start);

    ofstream outfile("wyniki_lista.csv");
    outfile << "Operacja,Czas_ms\n";
    outfile << "Tworzenie," << duration_insert.count() << "\n";
    outfile << "Wyszukiwanie," << duration_search.count() << "\n";
    outfile << "Usuwanie," << duration_delete.count() << "\n";
    outfile.close();

    cout << "Pomiar zakonczony. Wyniki zapisane w wyniki_lista.csv" << endl;

    return 0;
}
