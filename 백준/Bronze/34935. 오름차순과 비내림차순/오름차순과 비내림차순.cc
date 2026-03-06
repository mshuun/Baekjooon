#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;

    long long p, c;
    bool f = 1;

    if (n > 0)
        cin >> p;
    for (int i = 1; i < n; i++) {
        cin >> c;
        if (p == c)
            f = 0;
        p = c;
    }

    cout << f;
    return 0;
}