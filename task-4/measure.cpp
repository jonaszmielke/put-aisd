// measure.cpp
// Reads graphs g30_n.txt and g70_n.txt for n = 100,200,…,1500 from ./graphs/
// Measures Euler‐cycle (A) and Hamilton‐cycle (B) runtimes in nanoseconds,
// averaging the Hamiltonian measurement over multiple runs to avoid zero readings.
// Writes results into ./test_results/results_<label>.csv

#include <bits/stdc++.h>
using namespace std;

// --- load graph from file fn, setting n and adjacency list adj ---
void read_graph(const string &fn, int &n, vector<vector<int>> &adj) {
    ifstream in(fn);
    if (!in) {
        cerr << "Error: cannot open " << fn << "\n";
        exit(1);
    }
    int m;
    in >> n >> m;
    adj.assign(n, {});
    for (int i = 0, u, v; i < m; i++) {
        in >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
}

// --- Algorithm A: Eulerian cycle (Hierholzer) ---
vector<int> euler_cycle(const vector<vector<int>> &adj) {
    int n = adj.size();
    vector<multiset<int>> G(n);
    for (int u = 0; u < n; u++) {
        for (int v : adj[u]) {
            if (u < v) {
                G[u].insert(v);
                G[v].insert(u);
            }
        }
    }
    vector<int> st = {0}, tour;
    while (!st.empty()) {
        int v = st.back();
        if (G[v].empty()) {
            tour.push_back(v);
            st.pop_back();
        } else {
            int u = *G[v].begin();
            G[v].erase(G[v].find(u));
            G[u].erase(G[u].find(v));
            st.push_back(u);
        }
    }
    return tour;
}

// --- helper for Hamiltonian backtracking ---
bool backtrack(int v, int start,
               vector<int> &path,
               vector<bool> &used,
               const vector<vector<int>> &adj) {
    int n = adj.size();
    if ((int)path.size() == n) {
        for (int w : adj[v]) {
            if (w == start) {
                path.push_back(start);
                return true;
            }
        }
        return false;
    }
    for (int u : adj[v]) {
        if (!used[u]) {
            used[u] = true;
            path.push_back(u);
            if (backtrack(u, start, path, used, adj))
                return true;
            used[u] = false;
            path.pop_back();
        }
    }
    return false;
}

// --- Algorithm B: find first Hamiltonian cycle via backtracking ---
vector<int> ham_cycle(const vector<vector<int>> &adj) {
    int n = adj.size();
    vector<bool> used(n, false);
    vector<int> path;
    used[0] = true;
    path.push_back(0);
    if (backtrack(0, 0, path, used, adj))
        return path;
    else
        return {};
}

int main() {
    // We assume ./test_results/ already exists.
    vector<string> labels = {"30", "70"};

    // Number of repeats for Hamiltonian timing
    const int R = 200;

    for (const string &lbl : labels) {
        string outfn = "test_results/results_" + lbl + ".csv";
        ofstream out(outfn);
        if (!out) {
            cerr << "Error: cannot open " << outfn << " for writing\n";
            return 1;
        }
        // CSV header: Euler once, Hamilton average over R runs
        out << "n,t_euler_ns,t_hamilton_avg_ns\n";

        for (int n = 100; n <= 1500; n += 100) {
            string fn = "graphs/g" + lbl + "_" + to_string(n) + ".txt";

            vector<vector<int>> adj;
            int nn;
            read_graph(fn, nn, adj);

            // Measure Euler cycle once
            auto t1 = chrono::high_resolution_clock::now();
            euler_cycle(adj);
            auto t2 = chrono::high_resolution_clock::now();
            long long durE_ns = chrono::duration_cast<chrono::nanoseconds>(t2 - t1).count();

            // Measure Hamilton cycle R times and average
            long long sumH_ns = 0;
            for (int i = 0; i < R; ++i) {
                auto s = chrono::high_resolution_clock::now();
                ham_cycle(adj);
                auto e = chrono::high_resolution_clock::now();
                sumH_ns += chrono::duration_cast<chrono::nanoseconds>(e - s).count();
            }
            long long avgH_ns = sumH_ns / R;

            // Write to CSV
            out << n << "," << durE_ns << "," << avgH_ns << "\n";

            // Console log
            cout << "Measured n=" << n << " (" << lbl << "%): "
                 << durE_ns << " ns, avg " << avgH_ns << " ns\n";
        }

        cout << "Results saved to " << outfn << "\n";
    }

    return 0;
}
