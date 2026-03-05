#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, emo = 0;
    cin >> N;

    while (N--) {
        string S;
        cin >> S;
        if (S.find("01") != string::npos || S.find("OI") != string::npos) {
            emo++;
        }
    }

    cout << emo;

    return 0;
}