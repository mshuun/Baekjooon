#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string S;
    cin >> n >> S;
    for (int i = 0; i < n; i++) {
        if (S[i] == 'I') {
            S[i] = 'i';
        } else {
            S[i] = 'L';
        }
    }
    cout << S;
    return 0;
}