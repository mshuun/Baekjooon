#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<pair<int, vector<string>>> s = {
        {11, {"A","B","C","D","E","F","G","H","J","L","M"}},
        {9,  {"A","C","E","F","G","H","I","L","M"}},
        {9,  {"A","C","E","F","G","H","I","L","M"}},
        {9,  {"A","B","C","E","F","G","H","L","M"}},
        {8,  {"A","C","E","F","G","H","L","M"}},
        {8,  {"A","C","E","F","G","H","L","M"}},
        {8,  {"A","C","E","F","G","H","L","M"}},
        {8,  {"A","C","E","F","G","H","L","M"}},
        {8,  {"A","C","E","F","G","H","L","M"}},
        {8,  {"A","B","C","F","G","H","L","M"}}
    };

    auto &p = s[N - 1];
    cout << p.first << "\n";
    for (int i = 0; i < (int)p.second.size(); i++) {
        if (i) cout << ' ';
        cout << p.second[i];
    }
    cout << "\n";
    return 0;
}