#include <iostream>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    bool s = (a + b <= d), w = (c <= d);
    if (s && w)
        cout << "~.~";
    else if (!s && !w)
        cout << "T.T";
    else if (s)
        cout << "Shuttle";
    else
        cout << "Walk";
    return 0;
}