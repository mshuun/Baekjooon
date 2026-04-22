#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long double d, w;
    long long n;
    cin >> d >> w >> n;

    const long double pi = 3.14159L;
    long double need = w * (long double)n;
    long double have = pi * d;

    cout << (have + 1e-18L >= need ? "YES" : "NO") << "\n";
    return 0;
}