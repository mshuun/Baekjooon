#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int M[11], N, result = 0;
    double L[N];
    for (int i = 0; i < 11; i++)
        cin >> M[i];
    cin >> N;
    for (int i = 0; i < N; i++) {
        int B, S;
        double L;
        cin >> B >> L >> S;
        if (S >= 17 && L >= 2.0)
            result += M[B];
    }
    cout << result;
    return 0;
}