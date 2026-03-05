#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, a, b;
    cin >> N >> a >> b;
    N -= 2;
    int x = b - a;

    while (N--) {
        cin >> b;
    }
    cout << b + x;
    return 0;
}