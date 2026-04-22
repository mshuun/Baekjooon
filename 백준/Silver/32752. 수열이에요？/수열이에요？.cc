#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, L, R;
    cin >> N >> L >> R;

    vector<long long> A(N + 1);
    for (int i = 1; i <= N; i++) cin >> A[i];

    bool ok = true;

    for (int i = 1; i + 1 <= L - 1; i++) {
        if (A[i] > A[i + 1]) {
            ok = false;
            break;
        }
    }

    if (ok) {
        for (int i = R + 1; i < N; i++) {
            if (A[i] > A[i + 1]) {
                ok = false;
                break;
            }
        }
    }

    long long mn = A[L], mx = A[L];
    for (int i = L; i <= R; i++) {
        mn = min(mn, A[i]);
        mx = max(mx, A[i]);
    }

    if (L > 1 && A[L - 1] > mn) ok = false;
    if (R < N && mx > A[R + 1]) ok = false;

    cout << (ok ? 1 : 0) << '\n';
    return 0;
}