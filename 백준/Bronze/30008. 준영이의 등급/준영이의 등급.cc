#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, K, G, P, D;
    cin >> N >> K;
    for (int i = 0; i < K; i++) {
        cin >> G;
        P = G * 100 / N;
        if (96 < P) {
            D = 9;
        } else if (89 < P) {
            D = 8;
        } else if (77 < P) {
            D = 7;
        } else if (60 < P) {
            D = 6;
        } else if (40 < P) {
            D = 5;
        } else if (23 < P) {
            D = 4;
        } else if (11 < P) {
            D = 3;
        } else if (4 < P) {
            D = 2;
        } else {
            D = 1;
        }
        cout << D << " ";
    }
    return 0;
}