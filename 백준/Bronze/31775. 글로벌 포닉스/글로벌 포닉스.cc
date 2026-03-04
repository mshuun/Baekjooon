#include <iostream>
#include <string>

using namespace std;

int main() {
    int k = 0, l = 0, p = 0;
    string a;
    for (int i = 0; i < 3; i++) {
        cin >> a;
        if (a[0] == 'k') {
            k += 1;
        } else if (a[0] == 'l') {
            l += 1;
        } else if (a[0] == 'p') {
            p += 1;
        }
    }
    if (k == 1 && l == 1 && p == 1) {
        cout << "GLOBAL";
    } else {
        cout << "PONIX";
    }
    return 0;
}