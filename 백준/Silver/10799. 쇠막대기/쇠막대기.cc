#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    int op = 0;
    int total = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') {
            op++;
        } else {
            op--;
            if (s[i-1] == '(') {
                total += op;
            } else {
                total++;
            }
        }
    }

    cout << total << "\n";
    return 0;
}