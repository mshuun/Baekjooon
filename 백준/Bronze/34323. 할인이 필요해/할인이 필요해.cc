#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long N, M, S;
    cin >> N >> M >> S;

    long long discount = S * (100 - N) * (M + 1) / 100;

    long long plusone = M * S;

    if (discount < plusone) {
        cout << discount << "\n";
    } else {
        cout << plusone << "\n";
    }

    return 0;
}