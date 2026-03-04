#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int N, X, S, T, M = -1;
    cin >> N >> X;
    while (N--) {
        cin >> S >> T;
        if ((S + T) <= X) {
            M = max(M, S);
        }
    }
    cout << M;
    return 0;
}