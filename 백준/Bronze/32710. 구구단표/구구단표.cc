#include <iostream>
using namespace std;

int main() {
    int N, r = 0;
    cin >> N;
    for (int i = 2; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            r = N == i || N == j || N == i * j ? 1 : r;
        }
    }

    cout << r;
    return 0;
}