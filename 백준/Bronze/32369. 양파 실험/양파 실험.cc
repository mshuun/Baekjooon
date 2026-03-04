#include <iostream>

using namespace std;

int main() {
    int N, A, B, a = 1, b = 1, t;
    cin >> N >> A >> B;
    while (N--) {
        a += A;
        b += B;
        if (a < b) {
            t = a;
            a = b;
            b = t;
        } else if (a == b) {
            b -= 1;
        }
    }
    cout << a << " " << b;
    return 0;
}