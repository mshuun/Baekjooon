#include <iostream>

using namespace std;

int main() {
    int N, rage = 0;
    long long all_rage = 0;
    cin >> N;
    while (N--) {
        int rain;
        cin >> rain;
        rage += (rain ? 1 : -1);
        all_rage += rage;
    }
    cout << all_rage;
    return 0;
}