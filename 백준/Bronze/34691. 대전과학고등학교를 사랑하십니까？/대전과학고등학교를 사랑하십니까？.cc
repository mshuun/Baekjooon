#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    while (cin >> s && s != "end") {
        if (s == "animal") cout << "Panthera tigris\n";
        else if (s == "tree") cout << "Pinus densiflora\n";
        else if (s == "flower") cout << "Forsythia koreana\n";
    }
    return 0;
}