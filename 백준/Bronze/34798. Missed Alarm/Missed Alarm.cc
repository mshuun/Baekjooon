#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    cin >> a >> b;

    auto toMin = [&](const string& s) {
        int h = (s[0]-'0')*10 + (s[1]-'0');
        int m = (s[3]-'0')*10 + (s[4]-'0');
        return h*60 + m;
    };

    int A = toMin(a), B = toMin(b);
    cout << (B > A ? "YES" : "NO") << "\n";
    return 0;
}