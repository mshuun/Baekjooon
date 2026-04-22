#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    cin >> N;
    cout << (N * N <= 100000000LL ? "Accepted" : "Time limit exceeded") << "\n";
    return 0;
}