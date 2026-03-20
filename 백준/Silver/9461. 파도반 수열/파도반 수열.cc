#include <iostream>
using namespace std;

int main() {
    long long T, P[101] = {1, 1, 1, 2, 2};
    cin >> T;
    for (int i = 5; i < 101; i++) {
        P[i] = P[i - 5] + P[i - 1];
    }

    for (int i = 0; i < T; i++) {
        int a;
        cin >> a;
        cout << P[a - 1] << '\n';
    }
    return 0;
}