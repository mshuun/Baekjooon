#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, C, P;
    cin >> N >> C >> P;
    cout << (N <= C * P ? "yes" : "no") << "\n";
    return 0;
}