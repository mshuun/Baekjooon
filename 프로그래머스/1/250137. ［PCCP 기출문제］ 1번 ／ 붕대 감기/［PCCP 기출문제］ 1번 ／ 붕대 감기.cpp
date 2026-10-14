#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> bandage, int max_hp, vector<vector<int>> attacks) {
    int t = bandage[0], heal = bandage[1], bonus = bandage[2];
    int hp = max_hp, prev = 0;
    
    for (auto &a : attacks) {
        int gap = a[0] - prev - 1;
        hp = min(max_hp, hp + gap * heal + gap / t * bonus) - a[1];

        if (hp <= 0) return -1;
        prev = a[0];
    }
    return hp;
}