#include <cmath>
#include <iostream>

using namespace std;

bool is_square(int n) {
    int root = (int)sqrt(n);
    return root * root == n;
}

int main() {
    int n;
    cin >> n;

    if (is_square(n)) {
        cout << 1 << endl;
        return 0;
    }

    int temp_n = n;
    while (temp_n % 4 == 0)
        temp_n /= 4;
    if (temp_n % 8 == 7) {
        cout << 4 << endl;
        return 0;
    }

    for (int i = 1; i * i <= n; ++i) {
        if (is_square(n - i * i)) {
            cout << 2 << endl;
            return 0;
        }
    }

    cout << 3 << endl;

    return 0;
}