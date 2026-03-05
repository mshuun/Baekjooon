#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int X, Y;

    cin >> X >> Y;
    for (int i = 0; i < max(X, Y) - min(X, Y); i++)
        cout << 1;
    for (int i = 0; i < min(X, Y); i++) {
        cout << 2;
    }
    return 0;
}