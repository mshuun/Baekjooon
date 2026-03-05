#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M, A, B, chair;
    cin >> N >> M >> A >> B;
    chair = (N * 3 - M);
    cout << (chair <= 0 ? 0 : chair * A + B);
    return 0;
}