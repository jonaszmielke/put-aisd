#include <iostream>

using namespace std;

struct list {
    int info;
    struct list *next;
};

void insert(list *&head, int a) {
    if (head == nullptr) {
        // Create a new node and assign it as the head
        head = new list;
        head->info = a;
        head->next = nullptr;
    } else {
        if (head->info > a) {
            // Insert at the beginning
            list *tmp = new list;
            tmp->info = a;
            tmp->next = head;
            head = tmp;
        } else {
            // Traverse the list to find the correct position
            list *tmp = head;
            while (tmp->next != nullptr && tmp->next->info < a) {
                tmp = tmp->next;
            }
            // Insert the new node
            list *tmp2 = new list;
            tmp2->info = a;
            tmp2->next = tmp->next;
            tmp->next = tmp2;
        }
    }
}

void printList(list *head) {
    list *current = head;
    while (current != nullptr) {
        cout << current->info << " ";
        current = current->next;
    }
    cout << endl;
}

int main() {
    list *head = nullptr;

    int numbers[] = {3, 7, 1, 9, 5};
    int length = sizeof(numbers) / sizeof(numbers[0]);

    for (int i = 0; i < length; i++) {
        insert(head, numbers[i]);
    }

    printList(head);

    return 0;
}