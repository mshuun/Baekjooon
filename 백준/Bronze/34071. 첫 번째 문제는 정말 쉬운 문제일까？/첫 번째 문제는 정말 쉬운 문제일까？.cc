#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, first_x;
    cin >> N >> first_x;

    bool is_min = true;
    bool is_max = true;

    while (--N) {
        int x;
        cin >> x;

        if (x < first_x)
            is_min = false;
        if (x > first_x)
            is_max = false;
    }

    if (is_min) {
        cout << "ez";
    } else if (is_max) {
        cout << "hard";
    } else {
        cout << "?";
    }

    return 0;
}