#include <iostream>
#include <string>

using namespace std;

int main() {
    int N, A = 0, B = 0;
    string K;

    if (!(cin >> N >> K))
        return 0;

    for (int i = 0; i < N; i++) {
        if (K[i] & 1) {
            A++;
        } else {
            B++;
        }
    }

    cout << (A > B ? 1 : (B > A ? 0 : -1));

    return 0;
}