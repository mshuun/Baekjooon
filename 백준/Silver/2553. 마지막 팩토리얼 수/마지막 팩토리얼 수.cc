#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    long long res = 1;
    for (int i = 1; i <= n; i++) {
        res *= i;
        while (res % 10 == 0) {
            res /= 10;
        }
        res = res % 10000000;
    }
    cout << res % 10 << "\n";

    return 0;
}