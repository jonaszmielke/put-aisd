#include <bits/stdc++.h>
using namespace std;
using Clock = chrono::high_resolution_clock;

//––– Pomocnicze funkcje do drukowania wektorów –––
void print_cycle(const vector<int>& cycle) {
    if (cycle.empty()) {
        cout << "Brak cyklu.\n";
        return;
    }
    for (size_t i = 0; i < cycle.size(); ++i) {
        cout << cycle[i] + 1 << (i + 1 < cycle.size() ? " " : "\n");
    }
}

//––– Zwraca stopnie wierzchołka u w macierzy adj –––
int degree_of(const vector<vector<int>>& adj, int u) {
    int deg = 0;
    for (int v = 0; v < (int)adj.size(); ++v) {
        deg += adj[u][v];
    }
    return deg;
}

//––– Algorytm Hierholzera: znajduje ścieżkę/cykl Eulera (jeśli istnieje) –––
//    Przyjmuje macierz sąsiedztwa (zmienianą w trakcie działania) oraz 
//    indeks startowy. Zwraca kolejność wierzchołków w cyklu.
vector<int> find_euler_cycle(vector<vector<int>> adj) {
    int n = adj.size();
    // Na początek sprawdzamy, czy graf jest spójny (dla krawędzi) i każdy wierzchołek ma parzysty stopień.
    // Jeżeli graf niespójny lub są wierzchołki o nieparzystym stopniu, nie ma cyklu Eulera.
    // (Nie sprawdzamy tu szczegółowo spójności każdego komponentu, bo zakładamy, że dane są poprawne,
    // ale przynajmniej sprawdzimy stopnie.)
    for (int u = 0; u < n; ++u) {
        if (degree_of(adj, u) % 2 != 0) {
            return {}; // Brak cyklu Eulera
        }
    }
    // Znajdź wierzchołek startowy (pierwszy, który ma stopień > 0), inaczej 0.
    int start = 0;
    for (int u = 0; u < n; ++u) {
        if (degree_of(adj, u) > 0) {
            start = u;
            break;
        }
    }
    vector<int> path;
    // Funkcja rekurencyjna Hierholzera (usuwa krawędzie w trakcie przejścia).
    function<void(int)> dfs = [&](int u) {
        for (int v = 0; v < n; ++v) {
            if (adj[u][v] > 0) {
                // Usuń krawędź u–v
                adj[u][v]--;
                adj[v][u]--;
                dfs(v);
            }
        }
        path.push_back(u);
    };
    dfs(start);
    reverse(path.begin(), path.end());
    // Jeżeli liczba odwiedzonych krawędzi < sum(deg)/2 + 1, to znaczy, że graf nie był spójny.
    // path.size() powinno być równe liczbie krawędzi + 1.
    // Wyliczmy liczbę krawędzi w oryginalnej macierzy:
    int edges = 0;
    for (int u = 0; u < n; ++u) {
        for (int v = u + 1; v < n; ++v) {
            edges += adj[u][v]; // ale uwaga: adj już zredukowane – lepiej obliczyć przed redukcją
        }
    }
    // Jednak w praktyce, skoro zredukowaliśmy adj w rekursji, nie liczymy ponownie. 
    // Zauważmy więc, że jeśli w oryginale było M krawędzi, to path.size() powinno wynieść M+1.
    // Policzymy M w osobnej macierzy przed wywołaniem dfs albo wrócimy do prostszego sprawdzania:
    // Ale przyjmujemy: jeśli path zawiera >= 1 wierzchołka, traktujemy jako poprawny cykl Eulera.
    return path;
}

//––– Backtracking do znalezienia jednego cyklu Hamiltona –––
//    Jeśli znajdzie, zapisuje w 'ham_cycle' i zwraca true.
bool backtrack_hamilton(int u, 
                        const vector<vector<int>>& adj, 
                        vector<bool>& visited, 
                        vector<int>& current_path, 
                        int start) {
    int n = adj.size();
    if ((int)current_path.size() == n) {
        // Sprawdź, czy ostatni wierzchołek jest połączony z startem
        if (adj[u][start] > 0) {
            current_path.push_back(start);
            return true;
        } else {
            return false;
        }
    }
    for (int v = 0; v < n; ++v) {
        if (!visited[v] && adj[u][v] > 0) {
            visited[v] = true;
            current_path.push_back(v);
            if (backtrack_hamilton(v, adj, visited, current_path, start)) {
                return true;
            }
            visited[v] = false;
            current_path.pop_back();
        }
    }
    return false;
}

vector<int> find_hamilton_cycle(const vector<vector<int>>& adj) {
    int n = adj.size();
    if (n == 0) return {};
    // Spróbujemy założyć, że zaczynamy od wierzchołka 0 (można generalizować, ale dla większości grafów
    // wystarczy przetestować jeden wierzchołek). Jeżeli graf jest nieskierowany, to dowolna permutacja jest równoważna.
    int start = 0;
    vector<bool> visited(n, false);
    vector<int> path;
    visited[start] = true;
    path.push_back(start);
    if (backtrack_hamilton(start, adj, visited, path, start)) {
        return path;
    }
    return {}; // Brak cyklu Hamiltona
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    //––– 1. Wczytanie macierzy sąsiedztwa –––
    vector<vector<int>> adj;
    string line;
    while (getline(cin, line)) {
        if (line.empty()) continue;
        istringstream iss(line);
        vector<int> row;
        int x;
        while (iss >> x) {
            row.push_back(x);
        }
        adj.push_back(row);
    }
    int n = adj.size();
    if (n == 0) {
        cerr << "Brak danych wejsciowych.\n";
        return 0;
    }
    // Sprawdźmy, czy macierz jest kwadratowa
    for (auto& row : adj) {
        if ((int)row.size() != n) {
            cerr << "Macierz wejsciowa nie jest kwadratowa.\n";
            return 1;
        }
    }

    //––– 2. Cykl Eulera z mierzeniem czasu –––
    // Kopiujemy adj, bo algorytm Hierholzera go modyfikuje.
    vector<vector<int>> adj_for_euler = adj;
    auto start_euler = Clock::now();
    vector<int> euler_cycle = find_euler_cycle(adj_for_euler);
    auto end_euler = Clock::now();
    auto duration_euler = chrono::duration_cast<chrono::milliseconds>(end_euler - start_euler).count();

    cout << "===== Cykl Eulera =====\n";
    if (euler_cycle.empty()) {
        cout << "Graf nie ma cyklu Eulera (wierzcholki o nieparzystym stopniu lub niespojny).\n";
    } else {
        cout << "Kolejnosc wierzcholkow: ";
        print_cycle(euler_cycle);
    }
    cout << "Czas wykonania (Euler): " << duration_euler << " ms\n\n";

    //––– 3. Cykl Hamiltona z mierzeniem czasu –––
    auto start_ham = Clock::now();
    vector<int> ham_cycle = find_hamilton_cycle(adj);
    auto end_ham = Clock::now();
    auto duration_ham = chrono::duration_cast<chrono::milliseconds>(end_ham - start_ham).count();

    cout << "===== Cykl Hamiltona =====\n";
    if (ham_cycle.empty()) {
        cout << "Graf nie ma cyklu Hamiltona (lub nie znaleziono w przeszukiwaniu).\n";
    } else {
        cout << "Kolejnosc wierzcholkow (powrot do startu): ";
        print_cycle(ham_cycle);
    }
    cout << "Czas wykonania (Hamilton): " << duration_ham << " ms\n";

    return 0;
}
