// measure_all_hamilton.cpp
// Generates Hamiltonian undirected graphs with edge‐density 50% for n=3..12,
// enumerates all Hamiltonian cycles by pure backtracking (no reverse duplicates),
// measures the elapsed time averaged over multiple runs (with R chosen per n to avoid zeros),
// and writes results to test_results/hamilton_50.csv.
// Assumes directory "test_results" already exists.

#include <bits/stdc++.h>
/*
Windows probalby will show an error
bits/stdc++.h is a header exclusive to GNU Compiler Collection (GCC)
Nonetheless compiling this program on Windows using GCC executes without an error
And the program works as intended 
*/
using namespace std;
using ll = long long;

// Generate a Hamiltonian graph on n vertices with edge‐density p.
// Start from cycle 0–1–…–(n−1)–0, then add random edges.
vector<vector<int>> generate_graph(int n, double p, mt19937 &rng) {
    vector<set<int>> adj_set(n);
    set<pair<int,int>> edges;
    // Base cycle
    for (int i = 0; i < n; ++i) {
        int u = i, v = (i + 1) % n;
        adj_set[u].insert(v);
        adj_set[v].insert(u);
        edges.emplace(min(u,v), max(u,v));
    }
    int max_edges = n*(n-1)/2;
    int target = int(p * max_edges + 0.5);
    uniform_int_distribution<int> dist(0, n-1);
    while ((int)edges.size() < target) {
        int u = dist(rng), v = dist(rng);
        if (u == v) continue;
        auto e = make_pair(min(u,v), max(u,v));
        if (edges.insert(e).second) {
            adj_set[u].insert(v);
            adj_set[v].insert(u);
        }
    }
    vector<vector<int>> adj(n);
    for (int u = 0; u < n; ++u)
        adj[u].assign(adj_set[u].begin(), adj_set[u].end());
    return adj;
}

// Count all distinct Hamiltonian cycles via backtracking (no reversals).
ll count_hamilton_cycles(const vector<vector<int>> &adj) {
    int n = adj.size();
    vector<char> used(n,0);
    vector<int> path; path.reserve(n);
    used[0] = 1;
    path.push_back(0);
    ll count = 0;
    function<void(int)> dfs = [&](int u){
        if ((int)path.size() == n) {
            for (int w : adj[u]) {
                if (w == 0 && path[1] < path.back()) {
                    ++count;
                }
            }
            return;
        }
        for (int v : adj[u]) {
            if (!used[v]) {
                used[v] = 1;
                path.push_back(v);
                dfs(v);
                path.pop_back();
                used[v] = 0;
            }
        }
    };
    dfs(0);
    return count;
}

int main(){
    ofstream out("../results/hamilton_50.csv");
    if (!out) {
        cerr << "ERROR: cannot open task-4/results/hamilton_50.csv\n";
        return 1;
    }
    out << "n,cycles,avg_time_ns\n";

    mt19937 rng(12345);
    const double density = 0.5;

    // Loop n = 3..12
    for (int n = 3; n <= 12; ++n) {
        auto adj = generate_graph(n, density, rng);

        // Choose repetition count R so avg_time_ns > 0
        int R;
        if (n <= 5)      R = 100000;
        else if (n <= 7) R = 10000;
        else if (n <= 9) R = 1000;
        else if (n <= 11)R = 200;
        else             R = 100;

        // Warm up
        ll cycles = count_hamilton_cycles(adj);

        // Measure R runs
        ll total_ns = 0;
        for (int i = 0; i < R; ++i) {
            auto t0 = chrono::high_resolution_clock::now();
            count_hamilton_cycles(adj);
            auto t1 = chrono::high_resolution_clock::now();
            total_ns += chrono::duration_cast<chrono::nanoseconds>(t1 - t0).count();
        }
        ll avg_ns = total_ns / R;

        // Console log
        cout << "n=" << n
             << ", cycles=" << cycles
             << ", avg_time=" << avg_ns << " ns\n" << flush;

        // CSV
        out << n << "," << cycles << "," << avg_ns << "\n";
    }

    cout << "Results saved to task-4/results/hamilton_50.csv\n";
    return 0;
}
