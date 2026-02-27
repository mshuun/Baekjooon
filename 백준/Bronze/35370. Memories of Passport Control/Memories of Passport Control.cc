#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, s;
    cin >> k >> s;
    cout << (s / k) + (s % k) << "\n";
    return 0;
}