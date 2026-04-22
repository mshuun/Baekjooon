#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double S, D, T;
    cin >> S >> D >> T;
    double speed = S * 5280.0 / 3600.0;
    cout << (speed * T >= D ? "MADE IT" : "FAILED TEST") << "\n";
    return 0;
}