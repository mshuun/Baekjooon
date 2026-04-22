#include <iostream>

using namespace std;

int main() {
    int s, f;
    cin >> s >> f;
    if (s <= f) {
        cout << "high speed rail";
    } else {
        cout << "flight";
    }

    return 0;
}