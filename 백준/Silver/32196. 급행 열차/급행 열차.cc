#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, m, k, x, y;
    if (!(cin >> n >> m >> k >> x >> y)) return 0;

    vector<long long> diffs;
    diffs.reserve(n);

    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        diffs.push_back(a * x - b * y);
    }

    sort(diffs.begin(), diffs.end());

    long long sum_m = accumulate(diffs.begin(), diffs.begin() + m, 0LL);
    long long ans = k * (x + y) + sum_m;

    cout << ans << endl;

    return 0;
}