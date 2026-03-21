#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        int K;
        cin >> K;

        vector<int> lst(K);
        vector<long long> pfs(K + 1, 0);
        for (int i = 0; i < K; ++i) {
            cin >> lst[i];
            pfs[i + 1] = pfs[i] + lst[i];
        }

        vector<vector<long long>> DP(K, vector<long long>(K, 0));

        for (int n = 2; n <= K; ++n) {
            for (int i = 0; i <= K - n; ++i) {
                int j = i + n - 1;
                long long mini = LLONG_MAX;

                for (int k = i; k < j; ++k) {
                    long long cost = DP[i][k] + DP[k + 1][j];
                    if (cost < mini) mini = cost;
                }
                DP[i][j] = mini + (pfs[j + 1] - pfs[i]);
            }
        }

        cout << DP[0][K - 1] << "\n";
    }

    return 0;
}