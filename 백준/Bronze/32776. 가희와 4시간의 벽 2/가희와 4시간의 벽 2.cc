#include <iostream>

using namespace std;

int main() {
    int s, a, b, c;
    cin >> s >> a >> b >> c;
    s = s <= 240 ? -1 : s;
    cout << (s > a + b + c ? "flight" : "high speed rail");
    return 0;
}