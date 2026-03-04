#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    cout << (N % 2024 == 0 && N <= 100000 ? "Yes" : "No");
    return 0;
}