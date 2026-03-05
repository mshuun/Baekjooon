#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int N, emo = 0;
    cin >> N;
    while (N--) {
        string S;
        cin >> S;
        int len = S.length();
        for (int i = 0; i < len - 1; i++) {
            if (S[i] == '0' && S[i + 1] == '1') {
                emo++;
                break;
            } else if (S[i] == 'O' && S[i + 1] == 'I') {
                emo++;
                break;
            }
        }
    }
    cout << emo;
    return 0;
}