#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, curr, prev = 0, dp[3] = {0, 0, 0};
    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> curr;

        if (i == 0) {
            dp[2] = curr;
        } else if (i == 1) {
            dp[1] = dp[2];
            dp[2] += curr;
        } else if (i == 2) {
            dp[0] = dp[1];
            dp[1] = dp[2];
            dp[2] = max(dp[0], prev) + curr;
        } else {
            int next_dp = max(dp[1], dp[0] + prev) + curr;
            dp[0] = dp[1];
            dp[1] = dp[2];
            dp[2] = next_dp;
        }

        prev = curr;
    }

    if (N > 0)
        cout << dp[2] << "\n";

    return 0;
}