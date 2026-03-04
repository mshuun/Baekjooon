#include <iostream>

using namespace std;

int main() {
    int N, M, A[10], result = 0, select;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    cin >> M;
    while (M--) {
        cin >> select;
        result += A[select - 1];
    }

    cout << result;
    return 0;
}