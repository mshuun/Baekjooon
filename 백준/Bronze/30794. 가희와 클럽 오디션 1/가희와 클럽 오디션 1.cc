#include <iostream>
#include <string>
using namespace std;

int main() {
    int lv, score;
    string a;
    cin >> lv >> a;
    if (a == "miss") {
        score = 0;
    } else if (a == "bad") {
        score = 200 * lv;
    } else if (a == "cool") {
        score = 400 * lv;
    } else if (a == "great") {
        score = 600 * lv;
    } else if (a == "perfect") {
        score = 1000 * lv;
    }
    cout << score;
    return 0;
}