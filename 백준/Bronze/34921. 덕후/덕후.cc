#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, T;
    cin >> A >> T;
    int P = 10 + 2 * (25 - A + T);
    cout << max(0, P) << "\n";
    return 0;
}