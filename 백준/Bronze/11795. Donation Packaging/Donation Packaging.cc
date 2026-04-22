#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    int totalA = 0, totalB = 0, totalC = 0;

    while (t--) {
        int a, b, c;
        cin >> a >> b >> c;

        totalA += a;
        totalB += b;
        totalC += c;

        int package = min({totalA, totalB, totalC});

        if (package < 30) {
            cout << "NO\n";
        } else {
            cout << package << "\n";
            totalA -= package;
            totalB -= package;
            totalC -= package;
        }
    }

    return 0;
}