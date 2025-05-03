#include <iostream>

using namespace std;

class OneWayList
{
private:
    struct Node
    {
        int info;
        Node *next;
        Node(int v) : info(v), next(nullptr) {}
    };

    Node *head;

public:
    OneWayList() : head(nullptr) {}

    ~OneWayList()
    {
        while (head)
        {
            Node *tmp = head;
            head = head->next;
            delete tmp;
        }
    }

    void insert(int a)
    {
        if (!head)
        {
            head = new Node(a);
        }
        else if (head->info > a)
        {
            Node *tmp = new Node(a);
            tmp->next = head;
            head = tmp;
        }
        else
        {
            Node *curr = head;
            while (curr->next && curr->next->info < a)
            {
                curr = curr->next;
            }
            Node *tmp = new Node(a);
            tmp->next = curr->next;
            curr->next = tmp;
        }
    }

    bool search(int a) const
    {
        Node *curr = head;
        while (curr && curr->info <= a)
        {
            if (curr->info == a)
                return true;
            curr = curr->next;
        }
        return false;
    }

    void print() const
    {
        Node *curr = head;
        while (curr)
        {
            cout << curr->info << " ";
            curr = curr->next;
        }
        cout << "\n";
    }
};

/*
int main() {
    OneWayList *head = nullptr;

    int numbers[] = {3, 7, 1, 9, 5};
    int length = sizeof(numbers) / sizeof(numbers[0]);

    for (int i = 0; i < length; i++) {
        insert(head, numbers[i]);
    }

    printOneWayList(head);

    return 0;
}
*/