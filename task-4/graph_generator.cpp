// graph_generator.cpp
// Automatically generates connected undirected graphs on n = 100,200,…,1500
// vertices that are both Hamiltonian and Eulerian, at 30% and 70% edge‐densities.
// Outputs into subfolder "graphs/" as g30_<n>.txt and g70_<n>.txt.

#include <bits/stdc++.h>
using namespace std;
using pii = pair<int,int>;

// high-resolution RNG
static mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

// random in [0,1)
double rnd01() {
    return uniform_real_distribution<double>(0,1)(rng);
}

void generate_graph(int n, double p, const string &outf) {
    vector<set<int>> adj(n);
    vector<pii> edges;

    // 1) Hamiltonian cycle 0–1–…–(n−1)–0
    for (int i = 0; i < n; ++i) {
        int u = i, v = (i+1)%n;
        adj[u].insert(v);
        adj[v].insert(u);
        edges.emplace_back(u,v);
    }

    // 2) Add random edges up to target density
    int maxEdges = n*(n-1)/2;
    int targetM  = int(p * maxEdges + 0.5);
    while ((int)edges.size() < targetM) {
        int u = rng()%n, v = rng()%n;
        if (u==v || adj[u].count(v)) continue;
        adj[u].insert(v);
        adj[v].insert(u);
        edges.emplace_back(u,v);
    }

    // 3) Fix odd-degree vertices (pair them) for Eulerian property
    vector<int> odd;
    for (int i = 0; i < n; ++i)
        if (adj[i].size() % 2 == 1)
            odd.push_back(i);

    for (size_t i = 0; i+1 < odd.size(); i += 2) {
        int u = odd[i], v = odd[i+1];
        if (!adj[u].count(v)) {
            adj[u].insert(v);
            adj[v].insert(u);
            edges.emplace_back(u,v);
        } else {
            // find alternative partner
            for (int w = 0; w < n; ++w) {
                if (w!=u && !adj[u].count(w) && adj[w].size()%2==1) {
                    adj[u].insert(w);
                    adj[w].insert(u);
                    edges.emplace_back(u,w);
                    break;
                }
            }
        }
    }

    // 4) Write to file
    ofstream out(outf);
    if (!out) {
        cerr << "Error: cannot open " << outf << " for writing\n";
        exit(1);
    }
    out << n << " " << edges.size() << "\n";
    for (const auto &pr : edges) {
        out << pr.first << " " << pr.second << "\n";
    }
}

int main() {

    // densities and their labels
    vector<pair<double,string>> configs = {
        {0.30, "30"},
        {0.70, "70"}
    };

    // generate for n = 100,200,...,1500
    for (auto &cfg : configs) {
        double p = cfg.first;
        const string &lbl = cfg.second;
        for (int n = 8500; n <= 8500; n += 500) {
            string filename = "graphs/g" + lbl + "_" + to_string(n) + ".txt";
            cout << "Generating " << filename << "  (n=" << n
                 << ", density=" << p << ")\n";
            generate_graph(n, p, filename);
        }
    }

    cout << "All graphs generated in ./graphs/\n";
    return 0;
}
