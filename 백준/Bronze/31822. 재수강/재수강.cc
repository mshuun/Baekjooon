#include <iostream>
#include <string>

using namespace std;

int main() {
    int N, result;
    string code, newcode;
    cin >> code >> N;
    while (N--) {
        cin >> newcode;
        if (code.substr(0, 5) == newcode.substr(0, 5)) {
            result += 1;
        }
    }
    cout << result;
    return 0;
}