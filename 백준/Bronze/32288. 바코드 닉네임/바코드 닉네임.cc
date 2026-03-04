#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string S;
    cin >> n >> S;

    for (char &c : S) {
        if (c == 'I') {
            c = 'i';
        } else {
            c = 'L';
        }
    }

    cout << S;
    return 0;
}