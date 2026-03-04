#include <iostream>

using namespace std;

int main() {
    long long N;
    cin >> N;
    if (N > 2147483647 || N < -2147483648) {
        cout << "long long";
    } else if (N > 32767 || N < -32768) {
        cout << "int";
    } else {
        cout << "short";
    }
    return 0;
}