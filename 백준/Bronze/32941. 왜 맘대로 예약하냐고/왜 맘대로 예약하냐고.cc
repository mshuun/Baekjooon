#include <iostream>
using namespace std;

int main() {
    int T, X, N, r = 1;
    cin >> T >> X >> N;
    while (N--) {
        int Ki, Ai, rr = 0;
        cin >> Ki;
        while (Ki--) {
            cin >> Ai;
            rr = Ai == X ? 1 : rr;
        }
        r = rr == 0 ? 0 : r;
    }
    cout << (r ? "YES" : "NO");
    return 0;
}