#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int X, Y;
    cin >> X >> Y;

    cout << string(abs(X - Y), '1');
    cout << string(min(X, Y), '2');

    return 0;
}