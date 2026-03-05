#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T, t;
    cin >> T;
    while (T--) {
        cin >> t;
        cout << (t % 25 < 17 ? "ONLINE\n" : "OFFLINE\n");
    }
    return 0;
}