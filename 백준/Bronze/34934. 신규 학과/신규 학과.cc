#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, y;
    string s, r;
    cin >> n;
    while (n--) {
        cin >> s >> y;
        if (y == 2026) r = s;
    }
    cout << r;
    return 0;
}