#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    char c = s[0];
    if (c == 'F') cout << "Foundation\n";
    else if (c == 'C') cout << "Claves\n";
    else if (c == 'V') cout << "Veritas\n";
    else cout << "Exploration\n";
    return 0;
}